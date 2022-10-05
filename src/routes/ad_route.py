from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.ad_model import AdModel, UpdateAdModel
from src.services import ad_service

router = APIRouter(prefix="/ad")


@router.post("/", response_description="Add new ad", response_model=AdModel)
async def create_ad(ad: AdModel = Body(...)):
    """Function to handle the POST request to add a new ad to the ad collection

    :param ad: AdModel object containing the required tuple details
    :return: JSON object with the inserted tuple along with an HTTP response
    """
    created_ad = await ad_service.create_ad(ad)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ad)


@router.get("/", response_description="List all ads", response_model=List[AdModel])
async def list_ads():
    """Function to handle the GET request to list all the ads in the collection.

    :return: JSON objects with all the ads and an HTTP response
    """
    ads = await ad_service.list_ads()
    return JSONResponse(status_code=status.HTTP_200_OK, content=ads)


@router.get("/{id}", response_description="Get a single ad", response_model=AdModel)
async def get_ad(id: str):
    """Function to handle the GET request to get a particular ad from the collection.

    :param id: id of the ad to be retrieved.
    :type id: str
    :return: JSON object with the requested ad and HTTP response or an HTTP error
    """
    if (ad := await ad_service.get_ad(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=ad)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Ad {id} not found"
    )


@router.patch("/{id}", response_description="Update a ad", response_model=AdModel)
async def update_ad(id: str, ad: UpdateAdModel = Body(...)):
    """Function to handle the PATCH request to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param ad: UpdateAdModel object with the new details
    :return: JSON object with the updated details and HTTP response or an HTTP error
    """
    if (ad := await ad_service.update_ad(id, ad)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=ad)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Ad {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete an ad",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_ad(id: str):
    """Function to handle the DELETE request, to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: HTTP error response if the id not found
    """
    if not await ad_service.delete_ad(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Ad {id} not found"
        )
