from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / 'media'
VIDEOS_DIR = MEDIA_DIR / 'videos'

DATA_DIR = BASE_DIR / 'data'
DATA_IMG_DIR = DATA_DIR / 'img'
DATA_XML_DIR = DATA_DIR / 'xml'
DATA_CSV_DIR = DATA_DIR / 'csv'
DATA_MODEL_DIR = DATA_DIR / 'model'
