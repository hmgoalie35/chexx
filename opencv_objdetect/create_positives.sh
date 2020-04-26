#!/bin/bash

set -e

source utils.sh

print_step "Automatically generating positive images"
opencv_createsamples -img $SAMPLES_DIR/img/puck149_cropped.jpg -bg $BG_FILE -info $INFO_FILE -num 1000 -w $WIDTH -h $HEIGHT

print_step "Generating positives vector file for training"
opencv_createsamples -info $INFO_FILE -num 1000 -vec $VEC_FILE -w $WIDTH -h $HEIGHT
