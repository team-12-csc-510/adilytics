"""
This locust simulates the  users. To execute the script, use the following command:
locust -f locustfile.py --headless -H  http://127.0.0.1:8000 -u 10 -r 10

-u : No of users that will be spawned
-r : No of users spawned per second
"""

import json
from datetime import datetime
from random import choices, randint, randrange

from locust import HttpUser, task
from locust.exception import StopUser
from random_username.generate import generate_username


class QuickstartUser(HttpUser):
    def on_start(self):

        self.all_locations = self.client.get("/locations/")

        # all locations in a list of dictionary object;
        # each list element contains keys: "_id", "city", "state"
        self.all_locations = json.loads(self.all_locations.content)
        # #print(self.all_locations[0])

    @task
    def simulate_user(self):

        # Binary decision on whether existing user is chosen or new user is created.
        user_dec = randint(0, 1)
        # Create new user
        # #print("user_dec: ", user_dec)
        curr_user = None
        if user_dec == 0:

            # Get a random location from all_locations
            all_locations_ind = randrange(0, len(self.all_locations))
            # select location id
            rand_location_id = self.all_locations[all_locations_ind]["_id"]
            # print("The location selected:", self.all_locations[all_locations_ind])

            # Create and assign a random age.
            age = randrange(15, 80)

            username = generate_username(1)[0]
            email = username + "@gmail.com"

            created_at = datetime(
                year=datetime.now().year,
                month=randint(max(1, datetime.now().month - 6), datetime.now().month),
                day=randint(1, 28),
                hour=randint(0, 23),
                minute=randint(0, 59),
                second=randint(0, 59),
            )

            # #print(username)
            # #print(email)
            # #print(rand_location_id)
            # #print(age)

            params = {
                "name": username,
                "email": email,
                "location_id": rand_location_id,
                "age": age,
                "session": 1,
                "created_at": created_at,
                "updated_at": created_at,
            }
            # print("user post params:", params)

            curr_user = self.client.post("/user/", data=json.dumps(params, default=str))
            # print("New user created: ", curr_user.content)
            current_user = json.loads(curr_user.content.decode("utf-8"))
            # #print("current user:", curr_user)
        else:
            # Call an existing user
            all_users = self.client.get("/user/")
            # all_users contain list of dictionaries where each
            # list element contains dictionary with elements '_id', 'city', 'state'
            all_users = json.loads(all_users.content.decode("utf-8"))

            if not len(all_users):
                return

            # ##print(all_users)
            # get a random user from all_users list
            rand_user_ind = randrange(0, len(all_users))
            rand_user_id = all_users[rand_user_ind]["_id"]

            # Get the specific user whose id is fetched above.
            # Here the session id can be updated or another API call can be made to so.
            chosen_user = self.client.get("/user/" + rand_user_id).content
            current_user = json.loads(chosen_user.decode("utf-8"))

            # Update the session count of the chosen user
            new_session = current_user["session"] + 1
            self.client.patch(
                "/user/" + str(current_user["_id"]), json={"session": new_session}
            )

        # print("current_user:", current_user)

        all_ads = self.client.get("/ad/")
        all_ads = json.loads(all_ads.content.decode("utf-8"))
        display_active_ads = []
        active_ad_cnt = 0
        # Select 5 active ads which would be displayed to the user.
        while active_ad_cnt < 5:
            rand_ad_ind = randrange(0, len(all_ads))
            if all_ads[rand_ad_ind]["is_active"]:
                display_active_ads.append(all_ads[rand_ad_ind])
                active_ad_cnt += 1

        # #print("display active ads")
        # #print(display_active_ads)

        # Probability that user will click on any ad -> 33.33%
        # Probability that VIDEO ad is clicked  ->  50%
        # Probability that LARGE ad is clicked  ->  30%
        # Probability that MEDIUM ad is clicked ->  10%
        # Probability that SMALL ad is clicked  ->  05%

        rand_click_dec = randrange(0, 3)
        is_clicked = 0
        if rand_click_dec == 0:
            is_clicked = 1

        ad_weights = []
        for active_ad in display_active_ads:
            if active_ad["type"] == "SMALL":
                ad_weights.append(0.05)
            elif active_ad["type"] == "MEDIUM":
                ad_weights.append(0.1)
            elif active_ad["type"] == "LARGE":
                ad_weights.append(0.3)
            else:
                ad_weights.append(0.5)

        ad_clicked = choices(display_active_ads, ad_weights, k=is_clicked)

        if len(ad_clicked) == 1:
            # Create a click object
            ad_clicked = ad_clicked[0]
            ad_id = str(ad_clicked["_id"])
            user_id = str(current_user["_id"])
            created_at = datetime(
                year=datetime.now().year,
                month=randint(max(1, datetime.now().month - 6), datetime.now().month),
                day=randint(1, 28),
                hour=randint(0, 23),
                minute=randint(0, 59),
                second=randint(0, 59),
            )
            is_converted = False

            # call the create click service
            # ##print("ad_id:", ad_id)
            # ##print("user_id:", user_id)
            # ##print("is_converted:", is_converted)
            # ##print("created_at:", created_at)
            # ##print("updated_at:", created_at)

            params = {
                "ad_id": str(ad_id),
                "user_id": str(user_id),
                "is_converted": is_converted,
                "created_at": created_at,
                "updated_at": created_at,
            }
            # #print("params:", params)

            created_click = self.client.post(
                "/click/", data=json.dumps(params, default=str)
            )

            created_click = json.loads(created_click.content.decode("utf-8"))
            # There is 50 % chance that a clicked ad would be converted to a sale.
            rand_is_converted = randint(0, 1)
            if rand_is_converted == 0:
                # #print("Ad is converted")
                # call the update click service
                self.client.patch(
                    "/click/" + str(created_click["_id"]), json={"is_converted": True}
                )
        raise StopUser
