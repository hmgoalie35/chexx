import glob
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from conf import TRAINING_DIR


def xml_to_csv(path, train_file, test_file):
    train_list = []
    test_list = []
    i = 0
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            fname = Path('media/img/training/source') / root.find('filename').text
            value = (str(fname),
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )

            if i % 5 == 0:
                test_list.append(value)
            else:
                train_list.append(value)

        i += 1

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    pd.DataFrame(train_list, columns=column_name).to_csv(train_file, index=None)
    pd.DataFrame(test_list, columns=column_name).to_csv(test_file, index=None)


if __name__ == '__main__':
    csv_dir = TRAINING_DIR / 'csv'
    xml_to_csv(str(TRAINING_DIR / 'xml'), str(csv_dir / 'train.csv'), str(csv_dir / 'test.csv'))
