from conf import VIDEO_DIR
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker


if __name__ == '__main__':
    pt = PuckTracker(input_file=VIDEO_DIR / '20200408_223521.mp4')
    pt.run()

    et = EyeTracker(input_file=VIDEO_DIR / 'eye.mp4')
    # et.run()
