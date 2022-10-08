import unittest

import pytest
from httpx import AsyncClient

from src.main import app


class TestUserRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.User_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    @pytest.mark.anyio
    async def test_list_users(self):
        response = await self.client.get("/user/")
        assert len(response.json()) > 1

    @pytest.mark.anyio
    async def test_add_new_user(self):
        response = self.client.post(
            "/user/",
            json={
                "name": "Shubhender Singh",
                "email": "ssingh@rescue.com",
                "location_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "age": 27,
                "session": 1,
                "created_at": "2020-11-09T18:23:28+01:00",
                "updated_at": "2020-11-09T18:23:28+01:00",
            },
        )
        self.user_id = response.json()["_id"]
        assert response.status_code == 201
        assert response.json()["name"] == "Shubhender Singh"

    @pytest.mark.anyio
    async def test_get_specific_user(self):
        response = self.client.get(
            f"/user/{self.user_id}",
        )
        assert response.status_code == 200
        assert response.json()["email"] == "ssingh@rescue.com"

    @pytest.mark.anyio
    async def test_patch_specific_user(self):
        response = self.client.patch(
            f"/user/{self.user_id}",
            json={
                "name": "Shub Singh",
                "email": "ssingh@rescue.com",
                "location_id": "970f3bf7-96ec-47e8-8555-05aec91f92db",
                "age": 27,
                "session": 1,
                "created_at": "2020-11-09T18:23:28+01:00",
                "updated_at": "2020-11-09T18:23:28+01:00",
            },
        )
        assert response.status_code == 200
        assert response.json()["name"] == "Shub Singh"

    @pytest.mark.anyio
    async def test_delete_specific_user(self):
        response = self.client.delete(
            f"/user/{self.user_id}",
        )
        assert response.status_code == 204
