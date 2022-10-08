import asyncio
import unittest

from src.models.product_model import ProductModel
from src.services import product_service


class TestProductService(unittest.TestCase):
    def setUp(self):
        self.product_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_products(self):
        result = self.loop.run_until_complete(product_service.list_products())
        self.loop.close()
        assert result
        assert len(result) > 1

    async def test_create_product(self):
        product = ProductModel(name="product-zzz", cost=12.21)
        result = self.loop.run_until_complete(product_service.create_product(product))
        self.loop.close()
        assert result

        self.product_id = result["_id"]
        assert result["name"] == "product-zzz"

    async def test_get_product(self):
        result = self.loop.run_until_complete(
            product_service.get_product(self.product_id)
        )
        self.loop.close()
        assert result

        assert result["_id"] == self.product_id
        assert result["name"] == "product-zzz"

    async def test_delete_product(self):
        result = self.loop.run_until_complete(
            product_service.delete_product(self.product_id)
        )
        self.loop.close()

        assert result is True
