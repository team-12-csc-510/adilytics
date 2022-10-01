from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId


class AdModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company_id: str = Field(...)
    product_id: str = Field(...)
    type: str = Field(...)
    is_active: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "company_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "product_id": "40324d99-da33-4460-91bf-b29d85642851",
                "type": "SMALL",
                "is_active": True,
            }
        }


class UpdateAdModel(BaseModel):
    company_id: Optional[str]
    product_id: Optional[str]
    type: Optional[str]
    is_active: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "company_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "product_id": "40324d99-da33-4460-91bf-b29d85642851",
                "type": "SMALL",
                "is_active": True,
            }
        }
