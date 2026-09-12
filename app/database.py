from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

rutas_collection = db["rutas"]
servicios_collection = db["servicios"]
paraderos_collection = db["paraderos"]