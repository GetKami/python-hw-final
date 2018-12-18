from pprint import pprint
from urllib.parse import urlencode

import requests

APP_ID = 6773521
AUTH_URL = "https://oauth.vk.com/authorize?"

auth_data = {
    "client_id": APP_ID,
    "display": "page",
    "redirect_uri": "https://oauth.vk.com/blank.html",
    "response_type": "token",
    "v": "5.92"
}

token = "ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae"


class User:
    def __init__(self, screen_name):
        self.screen_name = screen_name

    def get_groups(self):
        params = {
            "screen_name": self.screen_name,
            "extended": 1,
            "fields": "members_count",
            "access_token": token,
            "v": "5.92"
        }

        response = requests.get("https://api.vk.com/method/groups.get",
                                params)
        return response.json()

    def get_friends(self):
        params = {
            "screen_name": self.screen_name,
            "access_token": token,
            "v": "5.92"
        }

        response = requests.get("https://api.vk.com/method/friends.get",
                                params)
        return response.json()

user_1 = User("eshmargunov")
pprint(user_1.get_groups())
pprint(user_1.get_friends())