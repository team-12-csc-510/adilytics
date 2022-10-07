from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.product_model import ProductModel
from src.services import product_service

router = APIRouter(prefix="/product")


@router.post("/", response_description="Add new product", response_model=ProductModel)
async def create_product(product: ProductModel = Body(...)):
    """Function to handle the POST request to add a new product to the product
     collection

    :param product: ProductModel object containing the required tuple details
    :return: JSON object with the inserted tuple along with an HTTP response
    """
    created_product = await product_service.create_product(product)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_product)


@router.get(
    "/", response_description="List all products", response_model=List[ProductModel]
)
async def list_products():
    """Function to handle the GET request to list all the products in the collection.

    :return: JSON objects with all the products and an HTTP response
    """
    products = await product_service.list_products()
    return JSONResponse(status_code=status.HTTP_200_OK, content=products)


@router.get(
    "/{id}", response_description="Get a single product", response_model=ProductModel
)
async def get_product(id: str):
    """Function to handle the GET request to get a particular product from the
    collection.

    :param id: id of the product to be retrieved.
    :type id: str
    :return: JSON object with the requested ad and HTTP response or an HTTP error
    """
    if (product := await product_service.get_product(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=product)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"product {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete a product",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(id: str):
    """Function to handle the DELETE request, to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: HTTP error response if the id not found
    """
    if not await product_service.delete_product(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {id} not found"
        )
