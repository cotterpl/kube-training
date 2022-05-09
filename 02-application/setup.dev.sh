#!/bin/bash

# This script setups the development environment for this service

echo "* Installing/upgrading pip"
# latest pip version is not compatible with pip-tools
pip install --upgrade pip
echo "* Installing/upgrading wheel"
pip install --upgrade wheel
echo "* Installing pip-tools"
pip install --upgrade pip-tools

echo "* Running pip-sync"
pip-sync requirements.txt || exit 1
echo "* Installing packages in the editable mode"
pip install --no-deps -e . || exit 2