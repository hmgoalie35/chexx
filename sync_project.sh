#!/bin/bash

set -e

source utils.sh

if [ "$1" == "--hard" ]; then
  print_step "Removing venv and node_modules"
  deactivate || true
  rm -rf venv/
  rm -rf node_modules/
fi

if [ ! -e venv ]; then
  print_step "Creating python virtual env"
  python3.7 -m venv venv/
fi

print_step "Installing python packages"
source venv/bin/activate && pip install -U pip && pip install -U -r requirements.txt

print_step "Installing node"
bash -ic "nvm install"

print_step "Install npm packages"
npm install
