#!/bin/bash

set -e

source utils.sh

sed -i s/\\/Users\\/mpittinsky\\/chexx\\/opencv_objdetect\\/samples\\/positives\\/// $INFO_FILE
