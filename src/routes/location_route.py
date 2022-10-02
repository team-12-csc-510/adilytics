from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.location_model import LocationModel, UpdateLocationModel
from src.services import location_service as location_service

router = APIRouter(prefix="/locations")


@router.post("/", response_description="Add new location", response_model=LocationModel)
async def create_location(location: LocationModel = Body(...)):
    created_location = await location_service.create_location(location)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_location)


@router.get(
    "/", response_description="List all locations", response_model=List[LocationModel]
)
async def list_locations():
    locations = await location_service.list_locations()
    return JSONResponse(status_code=status.HTTP_200_OK, content=locations)


@router.get(
    "/{id}", response_description="Get a single location", response_model=LocationModel
)
async def get_location(id: str):
    if (location := await location_service.get_location(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=location)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"location {id} not found"
    )


@router.patch(
    "/{id}", response_description="Update a location", response_model=LocationModel
)
async def update_location(id: str, location: UpdateLocationModel = Body(...)):
    if (location := await location_service.update_location(id, location)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=location)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"location {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete a location",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_location(id: str):
    if not await location_service.delete_location(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"location {id} not found"
        )
