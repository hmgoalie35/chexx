#!/bin/bash

set -e

source utils.sh

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

if [ ! -e $MODELS_DIR ]; then
  print_step "Cloning tensorflow models repo"
  git clone https://github.com/tensorflow/models.git $MODELS_DIR
fi

update_python_path

print_step "Compiling protobuf"
cd $RESEARCH_DIR
protoc object_detection/protos/*.proto --python_out=.

print_step "Testing tensorflow installation"
python object_detection/builders/model_builder_test.py

cd $DIR

print_step "Run ./part1.sh"
