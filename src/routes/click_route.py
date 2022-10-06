from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.click_model import ClickModel, UpdateClickModel
from src.services import click_service

router = APIRouter(prefix="/click")


@router.post("/", response_description="Add new click", response_model=ClickModel)
async def create_click(click: ClickModel = Body(...)):
    """
    Function to handle the POST request to add a new click to the click collection

    :param ad: ClickModel object containing the required tuple details
    :return: JSON object with the inserted tuple along with an HTTP response
    """
    created_click = await click_service.create_click(click)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_click)


@router.get(
    "/", response_description="List all clicks", response_model=List[ClickModel]
)
async def list_clicks():
    """
    Function to handle the GET request to list all the clicks in the collection.

    :return: JSON objects with all the ads and an HTTP response
    """
    clicks = await click_service.list_clicks()
    return JSONResponse(status_code=status.HTTP_200_OK, content=clicks)


@router.get(
    "/{id}", response_description="Get a single click", response_model=ClickModel
)
async def get_click(id: str):
    """
    Function to handle the GET request to get a particular click from the collection.

    :param id: id of the ad to be retrieved.
    :type id: str
    :return: JSON object with the requested ad and HTTP response or an HTTP error
    """
    if (click := await click_service.get_click(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=click)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Click {id} not found"
    )


@router.patch("/{id}", response_description="Update a click", response_model=ClickModel)
async def update_click(id: str, click: UpdateClickModel = Body(...)):
    """
    Function to handle the PATCH request to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param ad: UpdateClickModel object with the new details
    :return: JSON object with the updated details and HTTP response or an HTTP error
    """
    if (click := await click_service.update_click(id, click)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=click)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Click {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete a click",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_click(id: str):
    """
    Function to handle the DELETE request, to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: HTTP error response if the id not found
    """
    if not await click_service.delete_click(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Click {id} not found"
        )


@router.get(
    "/all/clicks30",
    response_description="List all clicks days",
    response_model=List[ClickModel],
)
async def list_clicks30d():
    """
    Function to get clicks generated in the past 30 days
    :return: Clicks in past 30 days
    """
    clicks = await click_service.list_all_clicks()
    return JSONResponse(status_code=status.HTTP_200_OK, content=clicks)
