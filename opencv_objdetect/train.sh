#!/bin/bash

set -e

source utils.sh

print_step "Training..."

opencv_traincascade -data $DATA_DIR -vec $VEC_FILE -bg $BG_FILE -numPos 500 -numNeg 500 0numStages 10 -w $WIDTH -h $HEIGHT
