from django.db import transaction
from .models import Shipment, Carrier
from logicore_common.schemas import ShipmentStatusChanged

class ShipmentService:
    @staticmethod
    def create_shipment(data: dict) -> Shipment:
        with transaction.atomic():
            # 1. Сохраняем в PostgreSQL
            shipment = Shipment.objects.create(**data)
            
            # 2. Здесь в реальном проекте вызывался бы асинхронный таск (Celery)
            # или продюсер Kafka для уведомления других систем.
            print(f"Shipment {shipment.tracking_number} created and indexed.")
            return shipment

    @staticmethod
    def update_status(shipment_id: int, new_status: str):
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.status = new_status
        shipment.save()
        
        # Имитация отправки события (мы реализуем это полностью на следующем этапе)
        event = ShipmentStatusChanged(
            shipment_id=shipment.id,
            new_status=new_status,
            location=shipment.destination
        )
        return event
    
    @staticmethod
    def trigger_status_notification(shipment_id: int, status: str, customer_email: str):
        """Интеграция с Celery воркером"""
        # delay() отправляет задачу в RabbitMQ
        from apps.notification_worker.tasks import send_shipment_notification
        task = send_shipment_notification.delay(shipment_id, status, customer_email)
        return task.id