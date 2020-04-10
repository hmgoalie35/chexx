import cv2 as cv

from conf import IMG_DIR, TRAINING_DIR, VIDEO_DIR
from readers.base import BaseReader


class Video2Img(BaseReader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0
        self.written = 375
        self.max = 500

    def handle_frame(self, frame):
        self.count += 1

        if self.written < self.max and self.count % 1 == 0:
            f = IMG_DIR / TRAINING_DIR / 'source' / f'puck{self.written}.jpg'
            cv.imwrite(str(f), frame)
            self.written += 1


if __name__ == '__main__':
    t = Video2Img(file_name=VIDEO_DIR / '20200408_223812.mp4')
    t.run()
