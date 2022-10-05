from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.product_model import ProductModel
from src.services import product_service

router = APIRouter(prefix="/product")


@router.post("/", response_description="Add new product", response_model=ProductModel)
async def create_product(product: ProductModel = Body(...)):
    created_product = await product_service.create_product(product)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_product)


@router.get(
    "/", response_description="List all products", response_model=List[ProductModel]
)
async def list_products():
    products = await product_service.list_products()
    return JSONResponse(status_code=status.HTTP_200_OK, content=products)


@router.get(
    "/{id}", response_description="Get a single product", response_model=ProductModel
)
async def get_product(id: str):
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
    if not await product_service.delete_product(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {id} not found"
        )
