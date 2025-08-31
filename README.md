# alx_travel_app_0x03

## Background Task Management with Celery and RabbitMQ

### Setup Instructions
1. Start RabbitMQ server:
   ```bash
   sudo service rabbitmq-server start
   ```
2. Run Django server:
   ```bash
   python manage.py runserver
   ```
3. Start Celery worker:
   ```bash
   celery -A alx_travel_app worker -l info
   ```

### Features
- Booking confirmation emails are sent asynchronously using Celery and RabbitMQ.
- Email backend is currently set to console (see logs in terminal).
- Update `EMAIL_BACKEND` in `settings.py` for real SMTP service.
