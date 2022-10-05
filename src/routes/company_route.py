from typing import List

from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

from src.models.company_model import CompanyModel, UpdateCompanyModel
from src.services import company_service

router = APIRouter(prefix="/company")


@router.post("/", response_description="Add new company", response_model=CompanyModel)
async def create_company(company: CompanyModel = Body(...)):
    """Function to handle the POST request to add a new ad to the company collection

    :param company: CompanyModel object containing the required tuple details
    :return: JSON object with the inserted tuple along with an HTTP response
    """
    created_company = await company_service.create_company(company)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_company)


@router.get(
    "/", response_description="List all companies", response_model=List[CompanyModel]
)
async def list_companies():
    """Function to handle the GET request to list all the companies in the collection.

    :return: JSON objects with all the companies and an HTTP response
    """
    companies = await company_service.list_companies()
    return JSONResponse(status_code=status.HTTP_200_OK, content=companies)


@router.get(
    "/{id}", response_description="Get a single user", response_model=CompanyModel
)
async def get_company(id: str):
    """Function to handle the GET request to get a particular company from the
    collection

    :param id: id of the company to be retrieved.
    :type id: str
    :return: JSON object with the requested ad and HTTP response or an HTTP error
    """
    if (company := await company_service.get_company(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=company)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Company {id} not found"
    )


@router.patch(
    "/{id}", response_description="Update a company", response_model=CompanyModel
)
async def update_company(id: str, company: UpdateCompanyModel = Body(...)):
    """Function to handle the PATCH request to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param company: UpdateCompanyModel object with the new details
    :return: JSON object with the updated details and HTTP response or an HTTP error
    """
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
    """Function to handle the DELETE request, to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: HTTP error response if the id not found"""
    if not await company_service.delete_company(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Company {id} not found"
        )
