from typing import List

from fastapi import APIRouter, Body, status, HTTPException
from fastapi.responses import JSONResponse

from src.models.user_model import UserModel
from src.services import user_service as user_service

router = APIRouter(prefix="/user")


@router.post("/", response_description="Add new user", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    created_user = await user_service.create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get(
    "/", response_description="List all users", response_model=List[UserModel]
)
async def list_users():
    users = await user_service.list_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@router.get(
    "/{id}", response_description="Get a single user", response_model=UserModel
)
async def get_user(user_id: str):
    if (user := user_service.get_user(user_id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student {id} not found")
