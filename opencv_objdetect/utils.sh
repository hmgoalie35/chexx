#!/bin/bash

set -e

DIR=$(pwd)
SAMPLES_DIR=$DIR/samples

POSITIVES_DIR=$SAMPLES_DIR/positives
INFO_FILE=$POSITIVES_DIR/info.txt
VEC_FILE=$POSITIVES_DIR/positives.vec

NEGATIVES_DIR=$SAMPLES_DIR/negatives
BG_FILE=$SAMPLES_DIR/bg.txt

DATA_DIR=$SAMPLES_DIR/data

TRAIN_WIDTH=20
TRAIN_HEIGHT=20


print_step() {
  printf "\n\n>>> $1\n\n"
}
