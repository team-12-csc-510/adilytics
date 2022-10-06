from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId
from src.utils import time_utils


class ClickModel(BaseModel):
    """
    Class to define the ClickModel object for defining the schema for the
    entries in the Click collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    ad_id: str = Field(...)
    user_id: str = Field(...)
    is_converted: bool = Field(...)
    created_at: datetime = time_utils.now()
    updated_at: datetime = time_utils.now()

    class Config:
        """
        Config class for the ClickModel class to define the schema example
        and also define the schema configuration.
        """

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "ad_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "user_id": "40324d99-da33-4460-91bf-b29d85642851",
                "is_converted": True,
                "created_at": "2020-11-09T18:23:28+01:00",
                "updated_at": "2020-11-09T18:23:28+01:00",
            }
        }


class UpdateClickModel(BaseModel):
    """
    Class to define the UpdateClickModel to create an object to update
    existing entry in the Click collection.
    """

    is_converted: Optional[bool]
    updated_at: Optional[datetime]

    class Config:
        """
        Config class to define the schema to update a particular entry in
        the Click collection.
        """

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {"is_converted": True, "updated_at": "2020-11-09T18:23:28+01:00"}
        }
