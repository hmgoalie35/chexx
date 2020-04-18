from conf import DATA_IMG_DIR, DATA_XML_DIR, VIDEOS_DIR
from utils.video import Video2Img
from utils.xml import strip_absolute_path
from trackers.chexx import ChexxTracker

if __name__ == '__main__':
    v2i = Video2Img(
        input_file=str(VIDEOS_DIR / 'chexx_player_view.mp4'),
        label='puck',
        output_dir=DATA_IMG_DIR,
        max_images=500,
        frequency=60,
        offset=0
    )
    strip_absolute_path(input_dir=DATA_XML_DIR)

    ct = ChexxTracker(input_file=str(VIDEOS_DIR / 'chexx_couch_view.mp4'))
    ct.run()
