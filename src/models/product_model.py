from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class ProductModel(BaseModel):
    """
    Class to define the ProductModel object for defining the schema for the
    entries in the Product collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    cost: float = Field(...)

    class Config:
        """
        Config class for the ProductModel class to define the schema example
        and also define the schema configuration.
        """

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Blue Bottle", "cost": 10.45}}


class UpdateProductModel(BaseModel):
    """
    Class to define the UpdateProductModel to create an object to update
    existing entry in the Product collection.
    """

    name: Optional[str]

    class Config:
        """
        Config class to define the schema to update a particular entry in
        the Product collection.
        """

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Blue Bottle", "cost": 10.45}}
