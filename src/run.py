from conf import VIDEO_DIR
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker


if __name__ == '__main__':
    pt = PuckTracker(file_name=VIDEO_DIR / '20200408_223521.mp4')
    pt.run()

    et = EyeTracker(file_name=VIDEO_DIR / 'eye.mp4')
    # et.run()
