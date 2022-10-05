from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class CompanyModel(BaseModel):
    """Class to define the CompanyModel object for defining the schema for the
    entries in the ad collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)

    class Config:
        """Config class for the CompanyModel class to define the schema example
        and also define the schema configuration.
        """

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Apple"}}


class UpdateCompanyModel(BaseModel):
    """Class to define the UpdateCompanyModel to create an object to update
    existing entry in the company collection.
    """

    name: Optional[str]

    class Config:
        """Config class to define the schema to update a particular entry in
        the company collection.
        """

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Apple"}}
