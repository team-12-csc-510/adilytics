import os
from dotenv import load_dotenv #to be commented added by aditya

from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore

load_dotenv() #to be commented added by aditya

client = AsyncIOMotorClient(os.getenv('MONGODB_URL')) #to be commented added by aditya
#client = AsyncIOMotorClient(os.environ["MONGODB_URL"]) #actual line

database = client.adilytics
