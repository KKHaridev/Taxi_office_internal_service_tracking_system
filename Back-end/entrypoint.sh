#!/bin/bash


python manage.py wait_for_db

# Perform database migrations
python3 manage.py migrate

# Start the Django development server
python3 manage.py runserver 0.0.0.0:8000