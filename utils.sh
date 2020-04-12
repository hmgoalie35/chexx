#!/bin/bash

set -e

DIR=$(pwd)
MODELS_DIR=$DIR/venv/lib/python3.7/site-packages/tensorflow/models
RESEARCH_DIR=$MODELS_DIR/research

DATA_DIR=$DIR/data
DATA_MODEL_DIR=$DATA_DIR/model

print_step() {
  printf "\n\n>>> $1\n\n"
}

update_python_path() {
  print_step "Updating pythonpath"
  export PYTHONPATH=$PYTHONPATH:$RESEARCH_DIR:$RESEARCH_DIR/slim
}
