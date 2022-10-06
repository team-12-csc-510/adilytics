from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.user_model import UpdateUserModel, UserModel
from src.services import user_service

router = APIRouter(prefix="/user")


@router.post("/", response_description="Add new user", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    """Function to handle the POST request to add a new user to the ad collection

    :param ad: UserModel object containing the required tuple details
    :return: JSON object with the inserted tuple along with an HTTP response
    """
    created_user = await user_service.create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get("/", response_description="List all users", response_model=List[UserModel])
async def list_users():
    """Function to handle the GET request to list all the users in the collection.

    :return: JSON objects with all the users and an HTTP response
    """
    users = await user_service.list_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=users)


@router.get("/{id}", response_description="Get a single user", response_model=UserModel)
async def get_user(id: str):
    """Function to handle the GET request to get a particular user from the collection.

    :param id: id of the user to be retrieved.
    :type id: str
    :return: JSON object with the requested user and HTTP response or an HTTP error
    """
    if (user := await user_service.get_user(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found"
    )


@router.patch("/{id}", response_description="Update a user", response_model=UserModel)
async def update_user(id: str, user: UpdateUserModel = Body(...)):
    """Function to handle the PATCH request to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param ad: UpdateUserModel object with the new details
    :return: JSON object with the updated details and HTTP response or an HTTP error
    """
    if (user := await user_service.update_user(id, user)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete a user",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(id: str):
    """Function to handle the DELETE request, to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: HTTP error response if the id not found
    """
    if not await user_service.delete_user(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found"
        )
