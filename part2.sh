#!/bin/bash

DIR=`pwd`
MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
cd $MODELS_DIR/research

export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

python object_detection/export_inference_graph.py \
  --input_type image_tensor \
  --pipeline_config_path ../ssd_mobilenet_v2_coco.config \
  --trained_checkpoint_prefix ../train/model.ckpt-0 \
  --output_directory ../fine_tuned_model

cp -r fine_tuned_model/* $DIR/data/model
