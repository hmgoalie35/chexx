#!/bin/bash

DIR=`pwd`
DATA_DIR=$DIR/data
DATA_MODEL_DIR=$DATA_DIR/model
MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
cd $MODELS_DIR/research

export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

cd ../ && rm -rf fine_tuned_model && cd research

python object_detection/export_inference_graph.py \
  --input_type image_tensor \
  --pipeline_config_path ../ssd_mobilenet_v2_coco.config \
  --trained_checkpoint_prefix ../train/model.ckpt-1600 \
  --output_directory ../fine_tuned_model

cp -r ../fine_tuned_model/* $DIR/data/model

python $DIR/src/tf_text_graph_ssd.py \
  --input=$DATA_MODEL_DIR/frozen_inference_graph.pb \
  --output=$DATA_MODEL_DIR/graph.pbtxt \
  --config=$DIR/src/ssd_mobilenet_v2_coco.config

sed -i s/AddV2/Add/g $DATA_MODEL_DIR/graph.pbtxt
