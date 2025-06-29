#!/bin/sh

set -e  # stop on error

echo "🔍 Waiting for MySQL"

while ! /usr/bin/mysqladmin ping -h db --silent; do
  echo "🔍"
  sleep 2
done

python manage.py makemigrations
python manage.py migrate
echo "🚀 Starting server..."
python -u manage.py runserver 0.0.0.0:8000
