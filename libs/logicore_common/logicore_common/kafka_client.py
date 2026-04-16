import json
import logging
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

logger = logging.getLogger(__name__)

class LogiCoreKafkaProducer:
    def __init__(self, bootstrap_servers: str):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    async def start(self):
        await self.producer.start()

    async def stop(self):
        await self.producer.stop()

    async def send_event(self, topic: str, data: dict):
        try:
            await self.producer.send_and_wait(topic, data)
        except Exception as e:
            logger.error(f"Failed to send event to Kafka: {e}")