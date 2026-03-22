#!/usr/bin/env bash
# exit on error
set -o errexit

export PYTHONPATH=$PYTHONPATH:.

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
