from conf import VIDEO_DIR
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker
from detect import detect


if __name__ == '__main__':
    chexx_vid = VIDEO_DIR / '20200408_223521.mp4'

    pt = PuckTracker(input_file=chexx_vid)
    # pt.run()

    et = EyeTracker(input_file=VIDEO_DIR / 'eye.mp4')
    # et.run()

    detect()
