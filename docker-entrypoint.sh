#!/usr/bin/env bash

# pip install ./
# pip list

cd ./sample/flask
pipenv install --system --deploy
pipenv run uwsgi --ini webapi.ini  --wsgi-file wsgi.py --http :9090
