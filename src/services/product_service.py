from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.product_model import ProductModel
from src.utils.database_const import Collections, Databases

product_db = Database()
product_db.database = Databases.adilytics.name
product_db.collection = Collections.product.name


async def create_product(product: ProductModel):
    product = jsonable_encoder(product)
    new_product = await product_db.collection.insert_one(product)
    created_product = await product_db.collection.find_one(
        {"_id": new_product.inserted_id}
    )
    return created_product


async def get_product(id: str):
    if (product := await product_db.collection.find_one({"_id": id})) is not None:
        return product


async def list_products(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    students = await product_db.collection.find().to_list(limit)
    return students


async def delete_product(id: str):
    delete_result = await product_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
