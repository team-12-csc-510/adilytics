import unittest

from httpx import AsyncClient

from src.main import app


class TestIndexRoute(unittest.TestCase):
    def setUp(self):
        self.client = self.load_client()
        self.Index_id = None

    async def load_client(self) -> AsyncClient:
        async with AsyncClient(app=app) as ac:
            return ac

    async def test_index_api(self):
        response = self.client.get(
            "/",
        )
        assert response.status_code == 201
