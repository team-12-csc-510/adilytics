from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class CompanyModel(BaseModel):
    """
    CompanyModel class used to define the database schema for the
    company collection in the Mongodb. It will provide the object that will
    be used to interact with the company cluster.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)

    class Config:
        """
        Config class for the CompanyModel class.
        defines the schema/format for the entries in this cluster
        along with the configurations for the accepted values for the
        fields.
        """
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Apple"}}


class UpdateCompanyModel(BaseModel):
    """
    UpdatedCompanyModel class to provide with the object that will
    be used to patch the entries for the company cluster.
    """
    name: Optional[str]

    class Config:
        """
        Config class for the UpdateCompanyModel class. Will provide
        configurations and schema format for the data used in the
        query to patch a particular entry using the UpdateCompanyModel
        class object.
        """
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Apple"}}
