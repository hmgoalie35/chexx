#!/bin/bash

MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
cd $MODELS_DIR

python research/object_detection/legacy/eval.py \
  --logtostderr \
  --pipeline_config_path=ssd_mobilenet_v2_coco.config \
  --checkpoint_dir=train \
  --eval_dir=eval
