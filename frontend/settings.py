import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

# Flask
sys.path.insert(0, str(BASE_DIR / 'apps'))
STATIC_FOLDER = str(BASE_DIR / 'static')
STATIC_URL = '/static'
TEMPLATE_FOLDER = str(BASE_DIR / 'templates')

# Obj detection
OBJ_DETECT_METHOD = os.environ.get('OBJ_DETECT_METHOD')
OBJ_DETECT_DIR = BASE_DIR / f'{OBJ_DETECT_METHOD}_objdetect'
DATA_DIR = OBJ_DETECT_DIR / 'data'
DATA_IMG_DIR = DATA_DIR / 'img'
DATA_XML_DIR = DATA_DIR / 'xml'
DATA_CSV_DIR = DATA_DIR / 'csv'
DATA_MODEL_DIR = DATA_DIR / 'model'
