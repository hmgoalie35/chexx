#!/bin/bash

set -e

source utils.sh

read -p "Are you sure? (Y/N): " confirm && [[ $confirm == [yY] ]] || exit 1

rm $POSITIVES_DIR/*.jpg
rm $INFO_FILE
rm $VEC_FILE
