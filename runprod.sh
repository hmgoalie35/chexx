#!/bin/bash

git pull && source venv/bin/activate && gunicorn -w 1 -t 10000000 --bind 0.0.0.0:5000 app
