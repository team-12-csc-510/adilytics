"""
This locust script will create ads that will be displayed to users.
Number of threads = number of ads to be created
"""
import json
from random import randint, randrange

from locust import HttpUser, task
from locust.exception import StopUser


class QuickstartUser(HttpUser):
    def on_start(self):

        self.ad_types = ["SMALL", "MEDIUM", "LARGE", "VIDEO"]

    @task
    def create_ads(self):

        rand_ad_ind = randrange(0, len(self.ad_types))
        ad_type = self.ad_types[rand_ad_ind]
        company_id = randrange(10e5, 10e8)

        # product_id will be randomly selected.
        # Get all the products.
        all_products = self.client.get("/product/")
        all_products = json.loads(all_products.content.decode("utf-8"))
        # print("All products:", all_products)
        rand_product_id = randrange(0, len(all_products))
        product_chosen = all_products[rand_product_id]
        product_chosen_id = product_chosen["_id"]

        is_active_decision = randint(0, 1)
        is_active = False
        if is_active_decision == 0:
            is_active = True

        self.client.post(
            "/ad/",
            json={
                "company_id": company_id,
                "product_id": product_chosen_id,
                "type": ad_type,
                "is_active": is_active,
            },
        )

        raise StopUser
