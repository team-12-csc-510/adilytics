"""
This locust script will create ads that will be displayed to users.
"""
import json
from random import randint, randrange

from locust import HttpUser, between, task
from locust.exception import StopUser
from random_username.generate import generate_username


class QuickstartUser(HttpUser):
    def on_start(self):

        self.all_locations = self.client.get("/locations/")

        # all locations in a list of dictionary object; each list element contains keys: "_id", "city", "state"
        self.all_locations = json.loads(self.all_locations.content)
        print(self.all_locations[0])

        self.ad_types = ["SMALL", "MEDIUM", "LARGE", "VIDEO"]

    @task
    def get_user(self):

        rand_ad_ind = randrange(0, len(self.ad_types))
        ad_type = self.ad_types[rand_ad_ind]
        company_id = randrange(10e5, 10e8)
        product_id = randrange(10e5, 10e8)

        is_active_decision = randint(0, 1)
        is_active = False
        if is_active_decision == 0:
            is_active = True

        self.client.post(
            "/ad/",
            json={
                "company_id": company_id,
                "product_id": product_id,
                "type": ad_type,
                "is_active": is_active,
            },
        )

        raise StopUser
