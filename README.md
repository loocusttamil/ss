celery -A stockproject beat -l info
celery -A stockproject.celery worker -l --pool=solo
