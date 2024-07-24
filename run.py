from datetime import datetime
import json

from eso_api import EsoApi
from eso_api import Headers
from eso_api.config.creds import API_KEY

if __name__ == "__main__":
    eso = EsoApi(Headers(api_key=API_KEY))

    date = datetime(2024, 3, 1, 0, 0, 0)
    with open("response/get_obejects.json", "w", encoding="utf-8") as f:
        response = eso.get_obejects(date)
        if not isinstance(response, list) and response.get("error"):
            print(response)
        else:
            print(response)
            f.write(json.dumps(response))
