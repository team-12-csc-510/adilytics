import unittest

import pytest
from httpx import AsyncClient

from src.main import app


class TestAdRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.ad_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    @pytest.mark.anyio
    async def test_list_ad(self):
        response = await self.client.get("/ad")
        assert len(response.json()) > 1

    @pytest.mark.anyio
    async def test_add_new_ad(self):
        response = self.client.post(
            "/ad/",
            json={
                "company_id": "random_id",
                "product_id": "random_id_2",
                "type": "SMALL",
                "is_active": False,
            },
        )
        self.ad_id = response.json()["_id"]
        assert response.status_code == 201
        assert response.json()["company_id"] == "random_id"

    @pytest.mark.anyio
    async def test_get_specific_ad(self):
        response = self.client.get(
            f"/ad/{self.ad_id}",
        )
        assert response.status_code == 200
        assert response.json()["company_id"] == "random_id"

    @pytest.mark.anyio
    async def test_patch_specific_ad(self):
        response = self.client.patch(
            f"/ad/{self.ad_id}",
            json={
                "company_id": "not_random_id",
                "product_id": "not_random_id_2",
            },
        )
        assert response.status_code == 200
        assert response.json()["company_id"] == "not_random_id"

    @pytest.mark.anyio
    async def test_delete_specific_click(self):
        response = self.client.delete(
            f"/ad/{self.ad_id}",
        )
        assert response.status_code == 204
