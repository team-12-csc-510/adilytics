import asyncio
import unittest

from src.models.user_model import UpdateUserModel, UserModel
from src.services import user_service


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_users(self):
        result = self.loop.run_until_complete(user_service.list_users())
        self.loop.close()
        assert result
        assert len(result) > 1

    async def test_create_user(self):
        user = UserModel(
            name="Shubhender Singh",
            email="ssingh@rescue.com",
            location_id="970f3bf7-96ec-47e8-8555-05aec91f92db",
            age=27,
            session=1,
            created_at="2020-11-09T18:23:28+01:00",
            updated_at="2020-11-09T18:23:28+01:00",
        )
        result = self.loop.run_until_complete(user_service.create_user(user))
        self.loop.close()
        assert result

        self.location_id = result["_id"]
        assert result["name"] == "Shubhender Singh"

    async def test_get_user(self):
        result = self.loop.run_until_complete(user_service.get_user(self.user_id))
        self.loop.close()
        assert result

        assert result["_id"] == self.location_id
        assert result["name"] == "Shubhender Singh"

    async def test_update_user(self):
        updated_user = UpdateUserModel(id=self.user_id, name="Shub Singh")
        result = self.loop.run_until_complete(
            user_service.update_user(self.user_id, updated_user)
        )
        self.loop.close()
        assert result

        assert result["name"] == "Shub Singh"

    async def test_new_user_count(self):
        result = self.loop.run_until_complete(user_service.get_new_users())
        self.loop.close()
        assert result
        assert result > 0

    async def test_user_sessions(self):
        result = self.loop.run_until_complete(user_service.get_total_sessions())
        self.loop.close()
        assert result
        assert result > 1

    async def test_get_user_info_with_location(self):
        result = self.loop.run_until_complete(
            user_service.get_user_info_with_location()
        )
        self.loop.close()
        assert result

        assert len(result) > 1

    async def test_delete_user(self):
        result = self.loop.run_until_complete(user_service.delete_user(self.user_id))
        self.loop.close()

        assert result is True
