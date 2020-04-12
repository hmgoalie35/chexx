from conf import VIDEO_DIR
from trackers.chexx import ChexxTracker
from trackers.eye import EyeTracker
from trackers.puck import PuckTracker


if __name__ == '__main__':
    chexx_vid = VIDEO_DIR / 'chexx_top_and_side_views.mp4'

    pt = PuckTracker(input_file=chexx_vid)
    # pt.run()

    et = EyeTracker(input_file=VIDEO_DIR / 'eye.mp4')
    # et.run()

    t = ChexxTracker(input_file=chexx_vid)
    t.run()
