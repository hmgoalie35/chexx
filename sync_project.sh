#!/bin/bash

print_step() {
  printf "\n\n>>> $1\n\n"
}

if [ "$1" == "--hard" ]; then
  print_step "Removing venv folder"
  deactivate || true
  rm -rf venv/
fi

if [ ! -e venv ]; then
  print_step "Creating python virtual env"
  python3.7 -m venv venv/
fi

print_step "Installing python packages"
source venv/bin/activate && pip install -U pip && pip install -U -r requirements.txt

print_step "Done"
