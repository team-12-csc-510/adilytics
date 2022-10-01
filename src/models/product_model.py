from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class ProductModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    cost: float = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Blue Bottle", "cost": 10.45}}


class UpdateProductModel(BaseModel):
    name: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Blue Bottle", "cost": 10.45}}
