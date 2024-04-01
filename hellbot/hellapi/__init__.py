import json
import os

import requests
from dotenv import load_dotenv

from hellbot.hellapi.datatypes import WarDetails

load_dotenv()

class HelldiversAPI:
    API_ROOT = os.getenv('API_ENDPOINT')
    STATUS_ENDPOINT = f'{API_ROOT}war/status'
    INFO_ENDPOINT = f'{API_ROOT}war/info'
    NEWS_ENDPOINT = f'{API_ROOT}war/news'
    CAMPAIGN_ENDPOINT = f'{API_ROOT}war/campaign'
    PLANETS_ENDPOINT = f'{API_ROOT}planets'
    PLANET_HISTORY_ENDPOINT = lambda self, planet: f"{self.API_ROOT}war/history/{planet}"

    def get_war_status(self) -> WarDetails:
        response = requests.get(self.STATUS_ENDPOINT)
        json_data = json.loads(response.content)
        details = WarDetails(**json_data)
        return details
    
    def get_planet_status(self):
        response = requests.get(self.PLANETS_ENDPOINT)
        json_data = json.loads(response.content)