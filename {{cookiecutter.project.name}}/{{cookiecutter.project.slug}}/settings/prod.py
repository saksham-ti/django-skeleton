from decouple import config
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


{%- if cookiecutter.database.sql %}
DATABASES = {
    'default': {
        'ENGINE': '{{ cookiecutter.database.sql.engine }}',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT"),
    }
}
{%- endif %}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL", "redis://redis:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_PREFIX": "wallstreet",
    }
}


# CELERY
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_EVENT_QUEUE_PREFIX = 'sakshammittal'