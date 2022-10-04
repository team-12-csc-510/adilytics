from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.click_model import ClickModel, UpdateClickModel
from src.services import click_service

router = APIRouter(prefix="/click")


@router.post("/", response_description="Add new click", response_model=ClickModel)
async def create_click(click: ClickModel = Body(...)):
    created_click = await click_service.create_click(click)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_click)


@router.get(
    "/", response_description="List all clicks", response_model=List[ClickModel]
)
async def list_clicks():
    clicks = await click_service.list_clicks()
    return JSONResponse(status_code=status.HTTP_200_OK, content=clicks)


@router.get(
    "/{id}", response_description="Get a single click", response_model=ClickModel
)
async def get_click(id: str):
    if (click := await click_service.get_click(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=click)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Click {id} not found"
    )


@router.patch("/{id}", response_description="Update a click", response_model=ClickModel)
async def update_click(id: str, click: UpdateClickModel = Body(...)):
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
    clicks = await click_service.list_all_clicks()
    return JSONResponse(status_code=status.HTTP_200_OK, content=clicks)
