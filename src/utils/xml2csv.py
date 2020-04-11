import glob
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from conf import DATA_IMG_DIR


def xml_to_csv(input_dir: Path, training_output_file: Path, testing_output_file: Path):
    train_list = []
    test_list = []
    i = 0
    for xml_file in glob.glob(str(input_dir / '*.xml')):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        rel_path = Path(root.find('path').text)
        abs_path = DATA_IMG_DIR / rel_path

        if not abs_path.exists():
            print(f'Could not locate img {abs_path} for xml file {xml_file}')
            continue

        abs_path_str = str(abs_path)

        for member in root.findall('object'):
            value = (
                abs_path_str,
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

    columns = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    pd.DataFrame(train_list, columns=columns).to_csv(str(training_output_file), index=None)
    pd.DataFrame(test_list, columns=columns).to_csv(str(testing_output_file), index=None)
