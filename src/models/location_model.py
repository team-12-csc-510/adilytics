from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class LocationModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    City: str = Field(...)
    State: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"City": "Raleigh",
                                    "State": "North Carolina"}}


class UpdateLocationModel(BaseModel):
    name: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"City": "Raleigh",
                                    "State": "North Carolina"}}
