# 실행 순서
# 1. venv 실행 --> 이 상태에서 start.ps1을 실행
Write-Host "Starting ASCT Project Services..."


# 2. Celery Worker (기존 창에서 실행)
celery -A config worker -l info -P eventlet

# 3. Celery Beat (기존 창에서 실행)
celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler 

# 4. Django Runserver (현재 창에서 실행)
python manage.py runserver 0.0.0.0:8000
