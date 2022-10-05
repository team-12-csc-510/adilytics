from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.company_model import CompanyModel, UpdateCompanyModel
from src.utils.database_const import Collections, Databases

company_db = Database()
company_db.database = Databases.adilytics.name
company_db.collection = Collections.company.name


async def create_company(company: CompanyModel):
    """
    function to insert the tuple into the company collection.

    :param company: CompanyModel object containing the tuple values.
    :type: company: CompanyModel object

    :returns: the created entry.
    """
    company = jsonable_encoder(company)
    new_company = await company_db.collection.insert_one(company)
    created_company = await company_db.collection.find_one(
        {"_id": new_company.inserted_id}
    )
    return created_company


async def list_companies(limit: int = 1000):
    """
    function to retrieve all the tuples from the collection.

    :param limit: limit for the number of tuples to be retrieved
    :type limit: int
    :return: all the entries in the company collection
    """
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    company_ls = await company_db.collection.find().to_list(limit)
    return company_ls


async def get_company(id: str):
    """
    function to fetch a particular tuple form the company collection.

    :param id: unique id for the tuple in the company collection
    :type id: str

    :returns: the requested tuple.
    """
    if (user := await company_db.collection.find_one({"_id": id})) is not None:
        return user


async def update_company(id: str, company: UpdateCompanyModel):
    """
    function for updating a tuple form the company collection.

    :param id: unique id for the tuple to be updated.
    :type: id: str

    :param company: UpdateCompanyModel object containing the updated tuple values.
    :type: company: UpdatedCompanyModel object

    :returns: the updated entry.
    """
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
    """
    function to  for deleting a tuple form the company collection.

    :param id: unique id for the tuple to be deleted.
    :type: id: str
    """
    delete_result = await company_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
