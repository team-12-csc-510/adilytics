from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId
from src.utils.ad_const import AdType


class AdModel(BaseModel):
    """Class to define the AdModel object for defining the schema for the
    entries in the ad collection.
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company_id: str = Field(...)
    product_id: str = Field(...)
    type: AdType = Field(...)
    is_active: bool = Field(...)

    class Config:
        """Config class for the AdModel class to define the schema example
        and also define the schema configuration.
        """

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
    """Class to define the UpdateAdModel to create an object to update
    existing entry in the ad collection.
    """

    company_id: Optional[str]
    product_id: Optional[str]
    type: Optional[str]
    is_active: Optional[bool]

    class Config:
        """Config class to define the schema to update a particular entry in
        the ad collection.
        """

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
