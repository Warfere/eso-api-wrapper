import requests
import datetime
import os, sys
from ..config.creds import api_key


print(datetime.datetime.now())

objectId = "12250124"
date = "2024-05-10T00:00:00+02:00"
url = f"https://api-dev.eso.lt/objects-api/v1/objects/json?date={date}"

headers = {
    "api-key": api_key,
    "X-B3-TraceId": "12b6e8e7-af40-45d6-8dfa-3ec901560ccd",
    # "objectId": objectId,
    "date": date,
}


def call():
    print("asdasd")
    print(os.getcwd())
    print(sys.path)
    with open("responses/test.json", "w", encoding="utf-8") as f:
        response = requests.get(url=url, headers=headers)
        f.write(response.text)


if __name__ == "__name__":
    call()
