import cv2 as cv

from readers.base import BaseReader


class Video2Img(BaseReader):
    def __init__(self, label, output_dir, max_images, frequency, offset=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.output_dir = output_dir
        self.offset = offset
        self.written_images = self.offset
        self.max_images = max_images
        self.frequency = frequency
        self._count = 0

    def handle_frame(self, frame):
        self._count += 1

        if (self.written_images - self.offset) < self.max_images and self._count % self.frequency == 0:
            file_name = str(self.output_dir / f'{self.label}{self.written_images}.jpg')
            cv.imwrite(file_name, frame)
            self.written_images += 1
            print(f'Wrote frame to {file_name}')
            return True
        elif (self.written_images - self.offset) > self.max_images:
            return False
