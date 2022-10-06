from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class LocationModel(BaseModel):
    """
    Class to define the LocationModel object for defining the schema for the
    entries in the Location collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    city: str = Field(...)
    state: str = Field(...)
    lat: float = Field(...)
    lon: float = Field(...)

    class Config:
        """
        Config class for the LocationModel class to define the schema example
        and also define the schema configuration.
        """

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

        schema_extra = {
            "example": {
                "city": "Raleigh",
                "state": "North Carolina",
                "lat": 1.555,
                "lon": 1.666,
            }
        }


class UpdateLocationModel(BaseModel):
    """
    Class to define the UpdateLocationModel to create an object to update
    existing entry in the Location collection.
    """

    city: Optional[str]
    state: Optional[str]
    lat: Optional[float]
    lon: Optional[float]

    class Config:
        """
        Config class to define the schema to update a particular entry in
        the Location collection.
        """

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {"city": "Raleigh", "state": "North Carolina"},
            "lat": 1.555,
            "lon": 1.666,
        }
