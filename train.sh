#!/bin/bash

MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
cd $MODELS_DIR

cd research && export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim && cd ..

python research/object_detection/legacy/train.py \
  --logtostderr \
  --train_dir=train \
  --pipeline_config_path=ssd_mobilenet_v2_coco.config
