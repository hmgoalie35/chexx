import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

# Flask
sys.path.insert(0, str(BASE_DIR / 'apps'))
STATIC_FOLDER = str(BASE_DIR / 'static')
STATIC_URL = '/static'
TEMPLATE_FOLDER = str(BASE_DIR / 'templates')

# Obj detection
OBJ_DETECT_METHOD = os.environ.get('OBJ_DETECT_METHOD')
OBJ_DETECT_DIR = PROJECT_DIR / f'{OBJ_DETECT_METHOD}_objdetect'

# Tensorflow
TF_DATA_DIR = OBJ_DETECT_DIR / 'data'
TF_DATA_MODEL_DIR = TF_DATA_DIR / 'model'
TF_FROZEN_INF_GRAPH_FILE = TF_DATA_MODEL_DIR / 'frozen_inference_graph.pb'
TF_GRAPH_FILE = TF_DATA_MODEL_DIR / 'graph.pbtxt'

# OpenCV
OPENCV_SAMPLES_DIR = OBJ_DETECT_DIR / 'samples'
OPENCV_DATA_DIR = OPENCV_SAMPLES_DIR / 'data'
OPENCV_CASCADE_FILE = OPENCV_DATA_DIR / 'cascade.xml'
