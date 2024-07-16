#!/bin/bash

celery -A tapp worker -l info &
env python3 manage.py runserver
pkill celery
