from pathlib import Path

import cv2 as cv


class BaseReader(object):
    def __init__(self, input_file):
        if isinstance(input_file, Path):
            input_file = str(input_file)
        self.input_file = input_file
        self.cap = None

    def open(self):
        self.cap = cv.VideoCapture(self.input_file)
        return self.cap.isOpened()

    def close(self):
        self.cap.release()
        cv.destroyAllWindows()

    def handle_frame(self, frame):
        raise NotImplementedError()

    def run(self):
        if not self.open():
            print(f'Unable to open {self.input_file}')
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.handle_frame(frame)
            if cv.waitKey(1) == 27:
                break
        self.close()
