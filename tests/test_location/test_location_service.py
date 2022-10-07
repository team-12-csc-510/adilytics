import asyncio
import unittest

from src.models.location_model import LocationModel, UpdateLocationModel
from src.services import location_service


class TestLocationService(unittest.TestCase):
    def setUp(self):
        self.location_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_locations(self):
        result = self.loop.run_until_complete(location_service.list_locations())
        self.loop.close()
        assert result
        assert len(result) > 1

    async def test_create_location(self):
        location = LocationModel(
            state="Random State", city="Random City", lat=1234.1234, lon=1234.1234
        )
        result = self.loop.run_until_complete(
            location_service.create_location(location)
        )
        self.loop.close()
        assert result

        self.location_id = result["_id"]
        assert result["city"] == "Random City"

    async def test_get_location(self):
        result = self.loop.run_until_complete(
            location_service.get_location(self.location_id)
        )
        self.loop.close()
        assert result

        assert result["_id"] == self.location_id
        assert result["city"] == "Random City"

    async def test_update_location(self):
        updated_location = UpdateLocationModel(
            id=self.location_id, city="Not a random city"
        )
        result = self.loop.run_until_complete(
            location_service.update_location(self.location_id, updated_location)
        )
        self.loop.close()
        assert result

        assert result["city"] == "Not a random city"

    async def test_delete_location(self):
        result = self.loop.run_until_complete(
            location_service.delete_location(self.location_id)
        )
        self.loop.close()

        assert result is True
