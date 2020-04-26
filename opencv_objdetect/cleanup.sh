#!/bin/bash

source utils.sh

read -p "Are you sure? (Y/N): " confirm && [[ $confirm == [yY] ]] || exit 1

rm $VEC_FILE
rm $DATA_DIR/*.xml
