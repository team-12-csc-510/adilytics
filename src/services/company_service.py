from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.company_model import CompanyModel, UpdateCompanyModel
from src.utils.database_const import Collections, Databases

company_db = Database()
company_db.database = Databases.adilytics.name
company_db.collection = Collections.company.name


async def create_company(company: CompanyModel):
    company = jsonable_encoder(company)
    new_company = await company_db.collection.insert_one(company)
    created_company = await company_db.collection.find_one(
        {"_id": new_company.inserted_id}
    )
    return created_company


async def list_companies(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    company_ls = await company_db.collection.find().to_list(limit)
    return company_ls


async def get_company(id: str):
    if (user := await company_db.collection.find_one({"_id": id})) is not None:
        return user


async def update_company(id: str, company: UpdateCompanyModel):
    company_dict: Dict[str, str] = {
        k: v for k, v in company.dict().items() if v is not None
    }

    if len(company_dict) >= 1:
        update_result = await company_db.collection.update_one(
            {"_id": id}, {"$set": company_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_company := await company_db.collection.find_one({"_id": id})
            ) is not None:
                return updated_company

    if (
        existing_company := await company_db.collection.find_one({"_id": id})
    ) is not None:
        return existing_company


async def delete_company(id: str):
    delete_result = await company_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
