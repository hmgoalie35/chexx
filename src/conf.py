from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / 'media'
VIDEO_DIR = MEDIA_DIR / 'video'

DATA_DIR = BASE_DIR / 'data'
DATA_IMG_DIR = DATA_DIR / 'img'
DATA_XML_DIR = DATA_DIR / 'xml'
