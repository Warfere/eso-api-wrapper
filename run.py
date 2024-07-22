from eso_api.api.eso import EsoApi
from eso_api.config.config import Config


config = Config()

eso = EsoApi(config)
date = "2024-05-10T00:00:00+02:00"
headers = {
    "api-key": config.settings.get("api_key"),
    "X-B3-TraceId": "12b6e8e7-af40-45d6-8dfa-3ec901560ccd",
    # "objectId": objectId,
    "date": date,
}


eso.getObejects(headers)
