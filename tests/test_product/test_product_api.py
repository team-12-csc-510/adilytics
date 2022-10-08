import unittest

import pytest
from httpx import AsyncClient

from src.main import app


class TestProductRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.product_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    @pytest.mark.anyio
    async def test_list_products(self):
        response = await self.client.get("/")
        assert len(response.json()) > 1

    @pytest.mark.anyio
    async def test_add_new_product(self):
        response = self.client.post(
            "/product/",
            json={
                "name": "product-xyz",
                "cost": 12.34,
            },
        )
        self.product_id = response.json()["_id"]
        assert response.status_code == 201
        assert response.json()["name"] == "product-xyz"

    @pytest.mark.anyio
    async def test_get_specific_product(self):
        response = self.client.get(
            f"/product/{self.product_id}",
        )
        assert response.status_code == 200
        assert response.json()["name"] == "product-xyz"

    @pytest.mark.anyio
    async def test_patch_specific_location(self):
        response = self.client.patch(
            f"/product/{self.product_id}",
            json={
                "name": "product-xyz",
                "cost": 34.21,
            },
        )
        assert response.status_code == 200
        assert response.json()["cost"] == 34.21

    @pytest.mark.anyio
    async def test_delete_specific_location(self):
        response = self.client.delete(
            f"/click/{self.click_id}",
        )
        assert response.status_code == 204
