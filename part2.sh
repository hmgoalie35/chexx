#!/bin/bash

set -e

source utils.sh

rm -rf $MODELS_DIR/fine_tuned_model

update_python_path

print_step "Generating inference graph"
python $RESEARCH_DIR/object_detection/export_inference_graph.py \
  --input_type image_tensor \
  --pipeline_config_path $MODELS_DIR/ssd_mobilenet_v2_coco.config \
  --trained_checkpoint_prefix $MODELS_DIR/train/model.ckpt-167 \
  --output_directory $MODELS_DIR/fine_tuned_model

print_step "Copying fine tuned model to project dir"
cp -r $MODELS_DIR/fine_tuned_model/* $DATA_MODEL_DIR

print_step "Generating graph for use by opencv"
python $DIR/src/tf_text_graph_ssd.py \
  --input=$DATA_MODEL_DIR/frozen_inference_graph.pb \
  --output=$DATA_MODEL_DIR/graph.pbtxt \
  --config=$DIR/src/ssd_mobilenet_v2_coco.config

sed -i s/AddV2/Add/g $DATA_MODEL_DIR/graph.pbtxt

print_step "Done!"
print_step "Run python src/run.py"
