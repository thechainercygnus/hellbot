import json
import os

import requests
from dotenv import load_dotenv

from hellbot.hellapi.datatypes import WarDetails, PlanetDetails

load_dotenv()

class HelldiversAPI:
    API_ROOT = os.getenv('API_ENDPOINT')
    STATUS_ENDPOINT = f'{API_ROOT}war/status'
    INFO_ENDPOINT = f'{API_ROOT}war/info'
    NEWS_ENDPOINT = f'{API_ROOT}war/news'
    CAMPAIGN_ENDPOINT = f'{API_ROOT}war/campaign'
    PLANETS_ENDPOINT = f'{API_ROOT}planets'
    PLANET_HISTORY_ENDPOINT = lambda self, planet: f"{self.API_ROOT}war/history/{planet}"

    def __init__(self):
        self.current_war_status = self.get_war_status()
        self.current_planet_status = self.get_planet_status()

    def get_war_status(self) -> WarDetails:
        response = requests.get(self.STATUS_ENDPOINT)
        json_data = json.loads(response.content)
        details = WarDetails(**json_data)
        return details
    
    def get_planet_status(self) -> list[PlanetDetails]:
        planet_statuses = []
        response = requests.get(self.PLANETS_ENDPOINT)
        json_data = json.loads(response.content)
        for planet_id in json_data:
            planet = json_data[planet_id]
            planet_statuses.append(PlanetDetails(planetId=planet_id, **planet))
        return planet_statuses
    
    def get_campaign_info(self):
        response = requests.get(self.CAMPAIGN_ENDPOINT)
        json_data = json.loads(response.content)
        return json_data