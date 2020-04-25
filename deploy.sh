#!/bin/bash

set -e


pkill gunicorn ; cd ~/chexx && git pull && ./runprod.sh
