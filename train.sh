#!/bin/bash

set -e

source utils.sh

update_python_path

cd $MODELS_DIR

python research/object_detection/legacy/train.py \
  --logtostderr \
  --pipeline_config_path=ssd_mobilenet_v2_coco.config \
  --train_dir=train

cd $DIR
