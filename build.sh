#!/bin/bash

# Install dependencies
pip3 install -r deps.txt

# Run collectstatic
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate