#!/bin/bash

set -e

SAMPLES_DIR=samples
BG_FILE=$SAMPLES_DIR/bg.txt

POSITIVES_DIR=$SAMPLES_DIR/positives
NEGATIVES_DIR=$SAMPLES_DIR/negatives
INFO_LST_FILE=$POSITIVES_DIR/info.lst
VEC_FILE=$POSITIVES_DIR/positives.vec

DATA_DIR=$SAMPLES_DIR/data

WIDTH=15
HEIGHT=13

print_step() {
  printf "\n\n>>> $1\n\n"
}
