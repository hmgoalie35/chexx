#!/bin/bash

export FLASK_APP=frontend/wsgi
export FLASK_ENV=development
export OBJ_DETECT_METHOD='opencv'
source venv/bin/activate && flask run
