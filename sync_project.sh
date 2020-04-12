#!/bin/bash

print_step() {
  printf "\n\n>>> $1\n\n"
}

if [ "$1" == "--hard" ]; then
  print_step "Removing venv folder"
  deactivate || true
  rm -rf venv/
fi

if [ ! -e venv ]; then
  print_step "Creating python virtual env"
  python3.7 -m venv venv/
fi

print_step "Installing python packages"
source venv/bin/activate && pip install -U pip && pip install -U -r requirements.txt

print_step "Cloning tensorflow models repo"
MODELS_DIR="venv/lib/python3.7/site-packages/tensorflow/models"
if [ ! -e $MODELS_DIR ]; then
  git clone https://github.com/tensorflow/models.git $MODELS_DIR
fi

print_step "Compiling protobuf"
cd $MODELS_DIR/research
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
python object_detection/builders/model_builder_test.py

print_step "Done"
