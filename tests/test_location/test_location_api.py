import unittest

import pytest
from httpx import AsyncClient

from src.main import app


class TestLocationRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.location_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    @pytest.mark.anyio
    async def test_list_locations(self):
        response = await self.client.get("/locations/")
        assert len(response.json()) > 1

    @pytest.mark.anyio
    async def test_add_new_location(self):
        response = self.client.post(
            "/locations/",
            json={
                "city": "Raleigh",
                "state": "North Carolina",
                "lat": 1234.1234,
                "lon": 1234.1234,
            },
        )
        self.location_id = response.json()["_id"]
        assert response.status_code == 201
        assert response.json()["city"] == "Raleigh"

    @pytest.mark.anyio
    async def test_get_specific_location(self):
        response = self.client.get(
            f"/locations/{self.location_id}",
        )
        assert response.status_code == 200
        assert response.json()["city"] == "Raleigh"

    @pytest.mark.anyio
    async def test_patch_specific_location(self):
        response = self.client.patch(
            f"/locations/{self.location_id}",
            json={
                "city": "Not Raleigh",
                "state": "North Carolina",
                "lat": 1234.1234,
                "lon": 1234.1234,
            },
        )
        assert response.status_code == 200
        assert response.json()["city"] == "Not Raleigh"

    @pytest.mark.anyio
    async def test_delete_specific_location(self):
        response = self.client.delete(
            f"/locations/{self.location_id}",
        )
        assert response.status_code == 204
