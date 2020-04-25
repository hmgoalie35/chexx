#!/bin/bash

set -e


ssh pi@192.168.1.20 "cd ~/chexx && git pull && ./runprod.sh"
