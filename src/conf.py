from pathlib import Path


BASE_DIR = Path('.').resolve().parent.parent
MEDIA_DIR = BASE_DIR / 'media'
IMG_DIR = MEDIA_DIR / 'img'
TRAINING_DIR = IMG_DIR / 'training'
VIDEO_DIR = MEDIA_DIR / 'video'
