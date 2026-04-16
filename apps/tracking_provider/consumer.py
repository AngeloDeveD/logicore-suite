import asyncio
import json
import logging
from aiokafka import AIOKafkaConsumer

logger = logging.getLogger(__name__)

async def start_tracking_consumer():
    consumer = AIOKafkaConsumer(
        'shipment_updates',
        bootstrap_servers='localhost:9092',
        group_id="tracking_group"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode('utf-8'))
            # Логика обработки: например, запись координат в MySQL
            logger.info(f"Received tracking data for shipment {data.get('shipment_id')}")
            await asyncio.sleep(0.1) # Имитация I/O
    finally:
        await consumer.stop()