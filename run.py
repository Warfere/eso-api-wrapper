from eso_api import EsoApi
from eso_api import Headers
from eso_api.config.creds import api_key
from datetime import datetime
import json

if __name__ == "__main__":
    eso = EsoApi(Headers(api_key=api_key))

    date = datetime(2024, 3, 1, 0, 0, 0)
    with open("response/getObejects.json", "w", encoding="utf-8") as f:
        response = eso.getObejects(date)
        if type(response) != list and response.get("error"):
            print(response)
        else:
            print(response)
            f.write(json.dumps(response))
