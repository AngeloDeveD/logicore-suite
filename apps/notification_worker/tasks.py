import logging
from .celery_app import app

logger = logging.getLogger(__name__)

@app.task(name="send_shipment_notification")
def send_shipment_notification(shipment_id: int, status: str, email: str):
    """Имитация отправки email-уведомления"""
    logger.info(f"Sending notification for Shipment {shipment_id}. New status: {status}")
    # В реальности здесь был бы вызов SendGrid, AWS SES или SMTP
    return f"Notification sent to {email}"