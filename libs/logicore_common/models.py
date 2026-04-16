from pydantic import BaseModel
from datetime import datetime

class BaseEvent(BaseModel):
    """Базовый класс для всех событий в системе (Kafka/RabbitMQ)"""
    event_id: str
    timestamp: datetime
    version: str = "1.0"

class ShipmentUpdateEvent(BaseEvent):
    """Событие обновления статуса груза"""
    shipment_id: int
    status: str
    location: str