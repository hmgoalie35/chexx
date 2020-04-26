#!/bin/bash

source utils.sh

if [ $# -ne 1 ]; then
  echo "Usage $0 <mode>"
  echo "  mode: choose from all or xml"
  exit 1
fi

read -p "Are you sure? (yY/N): " confirm && [[ $confirm == [yY] ]] || exit 1

if [ "$1" == "all" ]; then
  rm $VEC_FILE
fi

rm $DATA_DIR/*.xml
