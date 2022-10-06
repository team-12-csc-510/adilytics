from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

from src.models import PyObjectId
from src.utils import time_utils


class UserModel(BaseModel):
    """
    Model class for user. Defines the user collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    location_id: str = Field(...)
    age: int = Field(...)
    session: int = Field(...)
    created_at: datetime = time_utils.now()
    updated_at: datetime = time_utils.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Ritwik Tiwari",
                "email": "ritwik@example.com",
                "location_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "age": 25,
                "session": 1,
                "created_at": "2020-11-09T18:23:28+01:00",
                "updated_at": "2020-11-09T18:23:28+01:00",
            }
        }


class UpdateUserModel(BaseModel):
    """
    Config class for the UpdateUser class to define the schema example
    and also define the schema configuration.
    """

    name: Optional[str]
    email: Optional[EmailStr]
    location_id: Optional[str]
    age: Optional[int]
    session: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Ritwik Tiwari",
                "email": "ritwik@example.com",
                "location_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "age": 25,
                "session_id": "876a8c88-8458-4fee-b656-37decd4aa537",
            }
        }
