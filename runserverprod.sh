#!/bin/bash

npm run build

export FLASK_ENV=production
export OBJ_DETECT_METHOD='opencv'
git pull && source venv/bin/activate && gunicorn -w 1 -t 10000000 --bind 0.0.0.0:5000 frontend.wsgi
