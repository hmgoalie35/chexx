import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / 'media'
VIDEOS_DIR = MEDIA_DIR / 'videos'

DATA_DIR = BASE_DIR / 'data'
DATA_IMG_DIR = DATA_DIR / 'img'
DATA_XML_DIR = DATA_DIR / 'xml'
DATA_CSV_DIR = DATA_DIR / 'csv'
DATA_MODEL_DIR = DATA_DIR / 'model'


DEBUG = False
# Change this to dist if end up using webpack.
STATIC_FOLDER = str(BASE_DIR / 'static')
STATIC_URL = '/static'
TEMPLATE_FOLDER = str(BASE_DIR / 'templates')
APPS_DIR = str(BASE_DIR / 'apps')

sys.path.insert(0, APPS_DIR)

try:
    from .local import *
except ImportError:
    pass
