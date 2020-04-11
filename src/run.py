from conf import VIDEO_DIR
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker


if __name__ == '__main__':
    t = PuckTracker(file_name=VIDEO_DIR / '20200408_223521.mp4')
    t.run()

    t = EyeTracker(file_name=VIDEO_DIR / 'eye.mp4')
    t.run()
