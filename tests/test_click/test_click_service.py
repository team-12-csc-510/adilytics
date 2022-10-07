import asyncio
import unittest

from src.models.click_model import ClickModel, UpdateClickModel
from src.services import click_service


class TestClickService(unittest.TestCase):
    def setUp(self):
        self.click_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_clicks(self):
        result = self.loop.run_until_complete(click_service.list_clicks())
        self.loop.close()
        assert result
        assert len(result) > 1

    async def test_create_click(self):
        click = ClickModel(
            ad_id="random_ad_12",
            user_id="random_user_12",
            is_converted=True,
            created_at="2022-04-03T03:44:27",
            updated_at="2022-04-03T03:44:27",
        )
        result = self.loop.run_until_complete(click_service.create_click(click))
        self.loop.close()
        assert result

        self.click_id = result["_id"]
        assert result["ad_id"] == "random_ad_12"

    async def test_get_click(self):
        result = self.loop.run_until_complete(click_service.get_click(self.click_id))
        self.loop.close()
        assert result

        assert result["_id"] == self.click_id
        assert result["ad_id"] == "random_ad_12"

    async def test_update_click(self):
        updated_click = UpdateClickModel(id=self.click_id, ad_id="random_ad_112")
        result = self.loop.run_until_complete(
            click_service.update_click(self.click_id, updated_click)
        )
        self.loop.close()
        assert result

        assert result["ad_id"] == "random_ad_112"

    async def test_delete_click(self):
        result = self.loop.run_until_complete(click_service.delete_click(self.click_id))
        self.loop.close()

        assert result is True
