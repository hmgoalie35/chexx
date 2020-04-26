#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage $0 <env>"
  echo "  env: choose from dev or prod"
  exit 1
fi

export OBJ_DETECT_METHOD='opencv'
if [ "$1" == "dev" ]; then
  export FLASK_APP=frontend/wsgi
  export FLASK_ENV=development
  source venv/bin/activate && flask run
elif [ "$1" == "prod" ]; then
  npm run build
  export FLASK_ENV=production
  git pull && source venv/bin/activate && gunicorn -w 1 -t 10000000 --bind 0.0.0.0:5000 frontend.wsgi
fi
