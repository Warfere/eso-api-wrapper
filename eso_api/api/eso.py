import requests
from ..config.config import Config
from typing import Dict


class EsoApi:
    def __init__(self, config: Config) -> None:
        self.config = config
        if config.settings.get("api_key") is None:
            raise ValueError(message="Missing Api Key")

    def getObejects(self, headers: Dict) -> str:
        date = "2024-05-10T00:00:00+02:00"
        url = f"https://api-dev.eso.lt/objects-api/v1/objects/json?date={date}"
        return url
