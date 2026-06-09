# DRF Project

## Запуск через Docker

### 1. Создать .env

```bash
cp .env.example .env
```

Заполнить необходимые переменные.

### 2. Собрать контейнеры

```bash
docker-compose build
```

### 3. Запустить проект

```bash
docker-compose up -d
```

### 4. Применить миграции

```bash
docker-compose exec backend python manage.py migrate
```

### 5. Создать суперпользователя

```bash
docker-compose exec backend python manage.py createsuperuser
```

## Проверка сервисов

### Backend

```bash
docker ps
```

или

```bash
curl http://localhost:8000
```

### PostgreSQL

```bash
docker-compose exec db psql -U postgres
```

### Redis

```bash
docker-compose exec redis redis-cli ping
```

Ожидаемый ответ:

```text
PONG
```

### Celery

```bash
docker-compose logs celery
```

### Celery Beat

```bash
docker-compose logs celery-beat
```