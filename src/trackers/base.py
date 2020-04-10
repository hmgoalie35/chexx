from pathlib import Path

import cv2 as cv


class BaseTracker(object):
    def __init__(self, file_name):
        if isinstance(file_name, Path):
            file_name = str(file_name.resolve())
        self.file_name = file_name
        self.cap = None

    def open(self):
        self.cap = cv.VideoCapture(self.file_name)
        return self.cap.isOpened()

    def close(self):
        self.cap.release()
        cv.destroyAllWindows()

    def handle_frame(self, frame):
        raise NotImplementedError()

    def run(self):
        if not self.open():
            print(f'Unable to open {self.file_name}')
            return

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print('Reached end of stream')
                break
            self.handle_frame(frame)
            if cv.waitKey(30) == 27:
                break
        self.close()
