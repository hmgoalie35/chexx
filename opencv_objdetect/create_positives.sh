#!/bin/bash

set -e

source utils.sh

if [ $# -ne 1 ]; then
  echo "Usage $0 <mode>"
  echo "  mode: choose from auto or manual"
  exit 1
fi

if [ "$1" == "auto" ]; then
  print_step "Automatically generating positive images"
  opencv_createsamples -img $SAMPLES_DIR/img/puck149_cropped.jpg -bg $BG_FILE -info $INFO_FILE -num 1000
elif [ "$1" == "manual" ]; then
  print_step "Using manually generated positive images"
fi

print_step "Generating positives vector file for training"
opencv_createsamples -info $INFO_FILE -num 1000 -vec $VEC_FILE -w $TRAIN_WIDTH -h $TRAIN_HEIGHT
