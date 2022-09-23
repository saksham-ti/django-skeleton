from decouple import config
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

{%- if cookiecutter.database.sql.enabled %}
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

{%- if cookiecutter.storage.enabled %}
# Storages
{%- if cookiecutter.storage.s3.enabled %}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
AWS_S3_ACCESS_KEY_ID = config('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = config('AWS_S3_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN')
{%- endif %}
{%- if cookiecutter.storage.cloudinary.enabled %}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET')
}
{%- endif %}
{%- endif %}