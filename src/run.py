from conf import DATA_XML_DIR, VIDEO_DIR
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker
from utils.clean_xml import strip_absolute_path


if __name__ == '__main__':
    chexx_vid = VIDEO_DIR / '20200408_223521.mp4'

    pt = PuckTracker(input_file=chexx_vid)
    # pt.run()

    et = EyeTracker(input_file=VIDEO_DIR / 'eye.mp4')
    # et.run()

    strip_absolute_path(input_dir=DATA_XML_DIR)
