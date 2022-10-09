import unittest

import pytest
from httpx import AsyncClient

from src.main import app


class TestClickRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.click_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    @pytest.mark.anyio
    async def test_list_clicks(self):
        response = await self.client.get("/")
        assert len(response.json()) > 1

    @pytest.mark.anyio
    async def test_add_new_click(self):
        response = self.client.post(
            "/click/",
            json={
                "ad_id": "random_ad_123",
                "user_id": "random_user_123",
                "is_converted": True,
                "created_at": "2022-04-03T03:44:27",
                "updated_at": "2022-04-03T03:44:27",
            },
        )
        self.click_id = response.json()["_id"]
        assert response.status_code == 201
        assert response.json()["ad_id"] == "random_ad_123"

    @pytest.mark.anyio
    async def test_get_specific_click(self):
        response = self.client.get(
            f"/click/{self.click_id}",
        )
        assert response.status_code == 200
        assert response.json()["ad_id"] == "random_ad_123"

    @pytest.mark.anyio
    async def test_patch_specific_click(self):
        response = self.client.patch(
            f"/click/{self.click_id}",
            json={
                "ad_id": "random_ad_1234",
                "user_id": "random_user_123",
                "is_converted": True,
                "created_at": "2022-04-03T03:44:27",
                "updated_at": "2022-04-03T03:44:27",
            },
        )
        assert response.status_code == 200
        assert response.json()["ad_id"] == "random_ad_1234"

    @pytest.mark.anyio
    async def test_delete_specific_click(self):
        response = self.client.delete(
            f"/click/{self.click_id}",
        )
        assert response.status_code == 204
