from eso_api.api.eso import EsoApi
from eso_api.config.config import Config


def test_test():
    eso = EsoApi(Config())
    url = eso.getObejects({})
    assert url == "https://api-dev.eso.lt/objects-api/v1/objects/json?date=2024-05-10T00:00:00+02:00"
