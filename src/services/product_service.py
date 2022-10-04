from src.database.init_db import Database
from src.utils.database_const import Collections, Databases

product_db = Database()
product_db.database = Databases.adilytics.name
product_db.collection = Collections.product.name


async def get_product(id: str):
    if (product := await product_db.collection.find_one({"_id": id})) is not None:
        return product