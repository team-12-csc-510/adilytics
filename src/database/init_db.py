import os

from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore
from pymongo.errors import InvalidName

from src.utils.database_const import Collections, Databases

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])


class Database:
    def __int__(self):
        self._database = None
        self._collection = None

    @property
    def database(self):
        if self._database is None:
            raise InvalidName("Database is None")
        return self._database

    @database.setter
    def database(self, name: str):
        if not hasattr(Databases, name):
            raise InvalidName("Database name is Invalid")
        self._database = client[name]

    @property
    def collection(self):
        if self._collection is None:
            raise InvalidName("Collection name is None")
        return self._collection

    @collection.setter
    def collection(self, name: str):
        if not hasattr(Collections, name):
            raise InvalidName("Collection name is Invalid")
        self._collection = self.database[name]
