from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Thank you for your booking! Your booking ID is {booking_id}."
    from_email = "noreply@alxtravel.com"

    send_mail(subject, message, from_email, [to_email])
    return f"Email sent to {to_email} for booking {booking_id}"
