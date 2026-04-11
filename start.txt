# 실행 순서
Write-Host "Starting ASCT Project Services..."

# Redis 실행 (Docker CLI)
Write-Host "Starting Redis (Docker)..."
docker start my-redis 2>$null
if ($LASTEXITCODE -ne 0) {
    docker run -d --name my-redis -p 6379:6379 redis
}

# 1. docker의 redis server 실행

# 2. Django Runserver (현재 창에서 실행)
.\.venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000

# 3. Celery Worker (기존 창에서 실행)
celery -A config worker -l info -P eventlet

# 4. Celery Beat (기존 창에서 실행)
celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler