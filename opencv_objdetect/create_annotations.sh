#!/bin/bash

set -e

source utils.sh

opencv_annotation --annotations=$INFO_FILE --images=$IMGS_DIR
