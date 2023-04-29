#!/bin/sh

pip install virtualenv

virtualenv .venv  

source activate .venv

pip install -r requirements.txt