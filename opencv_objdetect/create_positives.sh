#!/bin/bash

set -e

source utils.sh

print_step "Automatically generating positive images"
opencv_createsamples -img samples/img/puck149_cropped.jpg -bg $BG_FILE -info $INFO_LST_FILE -w $WIDTH -h $HEIGHT -num 1000

print_step "Generating positives vector file for training"
opencv_createsamples -info $INFO_LST_FILE -num 1000 -w $WIDTH -h $HEIGHT -vec $VEC_FILE
