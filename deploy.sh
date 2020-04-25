#!/bin/bash

set -e


ssh pi@192.168.1.20 "pkill gunicorn && cd ~/chexx && git pull && screen -S gunicorn -d -m ./runprod.sh"
