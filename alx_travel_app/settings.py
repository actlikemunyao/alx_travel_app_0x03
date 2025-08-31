import os

INSTALLED_APPS = [
    # default Django apps...
    "listings",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@alxtravel.com"

# Celery configuration
CELERY_BROKER_URL = "amqp://localhost"  # RabbitMQ broker
CELERY_RESULT_BACKEND = "rpc://"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
