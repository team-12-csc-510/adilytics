import asyncio
import unittest

from src.services import index_service


class TestIndexService(unittest.TestCase):
    def setUp(self):
        self.user_id = None
        self.loop = asyncio.get_event_loop()

    async def test_list_users(self):
        result = self.loop.run_until_complete(index_service.create_obj())
        self.loop.close()
        assert result
        lis = ["click_count", "bounce_rate", "total_conversion"]
        lis.extend(["total_new_users", "sales", "visitors", "ads"])
        lis.extend(["revenue", "location_data"])
        for i in lis:
            assert i in result.keys()
