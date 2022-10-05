"""
This locust script will create products. The product_ids will be included in the ads.
Run a single thread for this locust script as the number of products to be created and posted are defined in a loop in the script.
"""
import json
from random import uniform

from locust import HttpUser, task
from locust.exception import StopUser

total_products = 50


class QuickstartUser(HttpUser):
    def on_start(self):

        self.total_products = total_products

    @task
    def create_products(self):

        # Create 50 products and post them in the database.
        all_products = ["Product%s" % i for i in range(1, self.total_products + 1)]
        product_cost = [
            round(uniform(100.00, 999.99), 2) for i in range(1, self.total_products + 1)
        ]
        for i in range(len(all_products)):
            params = {"name": all_products[i], "cost": product_cost[i]}
            product = self.client.post("/product/", data=json.dumps(params))

        raise StopUser
