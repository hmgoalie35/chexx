import glob
import xml.etree.ElementTree as ET
from pathlib import Path


def strip_absolute_path(input_dir: Path):
    """
    labelImg generates xml files with a `path` attribute being set to an absolute path.
    For portability b/w computers we only want to store relative paths, which will be converted to absolute paths when
    actually using the xml files.

    :param input_dir: Input directory containing xml files
    """
    for xml_file in glob.glob(str(input_dir / '*.xml')):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        path_el = root.find('path')
        abs_path = Path(path_el.text)
        rel_path = abs_path.name
        path_el.text = rel_path
        tree.write(xml_file)
