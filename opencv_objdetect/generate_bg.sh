#!/bin/bash

ls -d samples/negatives/*.jpg | sed 's/samples\///' > samples/bg.txt
