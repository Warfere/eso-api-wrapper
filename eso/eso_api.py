import requests
import datetime
from config.creds import api_key
print(datetime.datetime.now())

objectId = "12250124"
date = "2024-05-09T00:00:00+02:00"

url = f"https://api-dev.eso.lt/objects-api/v1/objects/json?date={date}"

headers = {
    "api-key": api_key,
    "X-B3-TraceId": "12b6e8e7-af40-45d6-8dfa-3ec901560ccd",
    # "objectId": objectId,
    "date": date,
}


with open("responses/test.json", "w", encoding="utf-8") as f:
    response = requests.get(url=url, headers=headers)
    f.write(response.text)

"""
requests.exceptions.ConnectTimeout: 
HTTPSConnectionPool(host='api-dev.eso.lt', port=443): 
Max retries exceeded with url: /objects-api/v1/objects/json?objectId=12250124&date=2024-07-09T00:00:00+02:00 
(Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000014BA19C6950>, 
'Connection to api-dev.eso.lt timed out. (connect timeout=None)'))
"""

