#!/bin/bash

set -e

tensorboard --logdir=./ --host=0.0.0.0
