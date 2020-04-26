#!/bin/bash

set -e

source utils.sh

print_step "Generating $BG_FILE"
ls -d $NEGATIVES_DIR/*.jpg | sed 's/samples\///' > $BG_FILE
