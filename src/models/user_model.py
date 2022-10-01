from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

from src.models import PyObjectId


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    location_id: str = Field(...)
    age: int = Field(...)
    session_id: str = Field(...)

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
                "session_id": "876a8c88-8458-4fee-b656-37decd4aa537",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    location_id: Optional[str]
    age: Optional[int]
    session_id: Optional[str]

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
