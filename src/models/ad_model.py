from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.models import PyObjectId
from src.utils.ad_const import AdType


class AdModel(BaseModel):
    """
    AdModel class used to define the database schema for the
    ads collection in the Mongodb. It will provide the object that will
    be used to interact with the ad cluster.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    company_id: str = Field(...)
    product_id: str = Field(...)
    type: AdType = Field(...)
    is_active: bool = Field(...)

    class Config:
        """
        Config class for the AdModel class.
        defines the schema/format for the entries in this cluster
        along with the configurations for the accepted values for the
        fields.
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
    """
    UpdatedAdModel class to provide with the object that will
    be used to patch the entries for the ad cluster.
    """
    company_id: Optional[str]
    product_id: Optional[str]
    type: Optional[str]
    is_active: Optional[bool]

    class Config:
        """
        Config class for the UpdateAdModel class. Will provide
        configurations and schema format for the data used in the
        query to patch a particular entry using the UpdateAdModel
        class object.
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
