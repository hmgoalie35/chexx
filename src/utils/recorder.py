import cv2 as cv
from readers.base import BaseReader
from .video import Video2Img


class Recorder(Video2Img):
    def open(self):
        ret = super().open()
        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
        return ret
