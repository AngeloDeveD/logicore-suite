import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .consumer import start_tracking_consumer

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запускаем консьюмер Kafka в фоновом режиме при старте
    task = asyncio.create_task(start_tracking_consumer())
    yield
    task.cancel()

app = FastAPI(title="LogiCore Tracking Provider", lifespan=lifespan)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "tracking_provider"}