import os

from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])

database = client.adilytics
