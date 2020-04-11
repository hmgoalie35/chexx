from pathlib import Path

import cv2 as cv

from readers.base import BaseReader


class Video2Img(BaseReader):
    def __init__(self, label: str, output_dir: Path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.output_dir = output_dir
        self.count = 0
        self.written = 0
        self.max = 500
        self.frequency = 1

    def handle_frame(self, frame):
        self.count += 1

        if self.written < self.max and self.count % self.frequency == 0:
            file_name = str(self.output_dir / f'{self.label}{self.written}.jpg')
            cv.imwrite(file_name, frame)
            self.written += 1
            print(f'Wrote frame to {file_name}')
