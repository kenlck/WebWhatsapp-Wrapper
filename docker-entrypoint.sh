#!/usr/bin/env bash

# pip install ./
# pip list

cd ./sample/flask
pipenv install
pipenv run uwsgi --ini WebAPI.ini  --wsgi-file wsgi.py --http :9090
