#!/bin/bash

set -e

SAMPLES_DIR=samples

POSITIVES_DIR=$SAMPLES_DIR/positives
INFO_FILE=$POSITIVES_DIR/info.txt
VEC_FILE=$POSITIVES_DIR/positives.vec

NEGATIVES_DIR=$SAMPLES_DIR/negatives
BG_FILE=$SAMPLES_DIR/bg.txt

DATA_DIR=$SAMPLES_DIR/data

WIDTH=15
HEIGHT=13

print_step() {
  printf "\n\n>>> $1\n\n"
}
