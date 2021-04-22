python3 manage.py migrate
gunicorn keyword_extractor.wsgi:application --bind 0.0.0.0:8000
