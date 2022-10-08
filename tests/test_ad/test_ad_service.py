import asyncio
import unittest

from src.models.ad_model import AdModel, UpdateAdModel
from src.services import ad_service


class TestAdService(unittest.TestCase):
    def setUp(self):
        self.ad_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_ads(self):
        result = self.loop.run_until_complete(ad_service.list_ads())
        self.loop.close()
        assert result
        assert len(result) > 1

    async def test_create_ad(self):

        ad = AdModel(
            company_id="random_company_id",
            product_id="random_product_id",
            type="SMALL",
            is_active=True,
        )
        result = self.loop.run_until_complete(ad_service.create_ad(ad))
        self.loop.close()
        assert result

        self.ad_id = result["_id"]
        assert result["company_id"] == "random_company_id"

    async def test_get_ad(self):
        result = self.loop.run_until_complete(ad_service.get_ad(self.ad_id))
        self.loop.close()
        assert result

        assert result["_id"] == self.ad_id
        assert result["company_id"] == "random_company_id"

    async def test_update_location(self):
        updated_ad = UpdateAdModel(id=self.ad_id, company_id="not_random_company_id")
        result = self.loop.run_until_complete(
            ad_service.update_ad(self.ad_id, updated_ad)
        )
        self.loop.close()
        assert result

        assert result["company_id"] == "not_random_company_id"

    async def test_delete_location(self):
        result = self.loop.run_until_complete(ad_service.delete_ad(self.ad_id))
        self.loop.close()

        assert result is True
