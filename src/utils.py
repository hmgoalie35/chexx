import glob
import xml.etree.ElementTree as ET
from pathlib import Path

import cv2 as cv
import pandas as pd

from conf import IMG_DIR, TRAINING_DIR
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


def xml_to_csv(path, out_file):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            fname = Path('../media/img/training/source') / root.find('filename').text
            value = (str(fname),
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv(out_file, index=None)


if __name__ == '__main__':
    xml_to_csv(str(TRAINING_DIR / 'xml'), str(TRAINING_DIR / 'csv' / 'output.csv'))
