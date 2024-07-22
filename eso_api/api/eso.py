from .call import Call
from ..config.headers import Headers
from datetime import datetime
from .errors import EsoError
from typing import Dict


class EsoApi(Call):
    #TODO: return type from error and good response is list
    #TODO: server side error returs 200 
    #TODO: review headers class. Headers class is been passed. Need to decide if passing class or dict
    def __init__(self, headers: Headers, environment="dev") -> None:
        self.headers = headers
        self.environment = environment

    def getObejects(self, date: datetime, objectId: int = None) -> Dict:
        url = f"objects-api/v1/objects/json?date={self.format_date(date)}"
        if objectId:
            url += f"&objectId={objectId}"
        try:
            print(type(self.headers))
            response = self.get(url, self.headers)
            return response
        except EsoError as e:
            return {"error": e}

    def format_date(self, date: datetime) -> str:
        return date.astimezone().replace(microsecond=0).isoformat()
