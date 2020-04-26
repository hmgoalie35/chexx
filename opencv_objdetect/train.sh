#!/bin/bash

set -e

source utils.sh

print_step "Training"

cd $SAMPLES_DIR

opencv_traincascade \
  -data $(basename $DATA_DIR) \
  -vec $VEC_FILE \
  -bg $(basename $BG_FILE) \
  -numPos 1003 \
  -numNeg 500 \
  -numStages 15
