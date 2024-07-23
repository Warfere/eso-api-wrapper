from datetime import datetime
from typing import Dict
from .call import Call
from ..config.headers import Headers
from .errors import EsoError


# pylint: disable=fixme
class EsoApi(Call):
    # TODO: return type from error and good response is list
    # TODO: server side error returs 200
    # TODO: review headers class. Headers class is been passed.
    # Need to decide if passing class or dict
    def __init__(self, headers: Headers, environment="dev") -> None:
        self.headers = headers
        self.environment = environment

    def get_obejects(self, date: datetime, object_id: int = None) -> Dict:
        url = f"objects-api/v1/objects/json?date={self.format_date(date)}"
        if object_id:
            url += f"&object_id={object_id}"
        try:
            print(type(self.headers))
            response = self.get(url, self.headers)
            return response
        except EsoError as e:
            return {"error": e}

    def format_date(self, date: datetime) -> str:
        return date.astimezone().replace(microsecond=0).isoformat()
