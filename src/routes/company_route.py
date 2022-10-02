from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.company_model import CompanyModel, UpdateCompanyModel
from src.services import company_service

router = APIRouter(prefix="/company")


@router.post("/", response_description="Add new company", response_model=CompanyModel)
async def create_company(company: CompanyModel = Body(...)):
    created_company = await company_service.create_company(company)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_company)


@router.get(
    "/", response_description="List all companies", response_model=List[CompanyModel]
)
async def list_companies():
    companies = await company_service.list_companies()
    return JSONResponse(status_code=status.HTTP_200_OK, content=companies)


@router.get(
    "/{id}", response_description="Get a single user", response_model=CompanyModel
)
async def get_company(id: str):
    if (company := await company_service.get_company(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=company)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Company {id} not found"
    )


@router.patch(
    "/{id}", response_description="Update a company", response_model=CompanyModel
)
async def update_company(id: str, company: UpdateCompanyModel = Body(...)):
    if (company := await company_service.update_company(id, company)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=company)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Company {id} not found"
    )


@router.delete(
    "/{id}",
    response_description="Delete a company",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_company(id: str):
    if not await company_service.delete_company(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Company {id} not found"
        )
