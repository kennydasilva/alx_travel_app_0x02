from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(booking_reference):
    send_mail(
        "Pagamento Confirmado",
        f"Sua reserva {booking_reference} foi paga com sucesso.",
        "noreply@travelapp.com",
        ["cliente@email.com"],
    )
