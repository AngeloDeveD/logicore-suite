import json

def kafka_serializer(value):
    """Универсальный сериализатор для Kafka"""
    if isinstance(value, dict):
        return json.dumps(value).encode('utf-8')
    return value.json().encode('utf-8')