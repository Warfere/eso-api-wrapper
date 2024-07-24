from datetime import datetime
from typing import List, Optional
from .call import Call
from ..config.headers import Headers


# pylint: disable=fixme
class EsoApi(Call):
    # TODO: return type from error and good response is list
    # TODO: review headers class. Headers class is been passed.
    def __init__(self, headers: Headers, environment="dev") -> None:
        self.headers = headers
        self.environment = environment

    def get_obejects(self, date: datetime, object_id: Optional[int] = None) -> List:
        url = f"objects-api/v1/objects/json?date={self.format_date(date)}"
        if object_id:
            url += f"&object_id={object_id}"
        return self.get(url, self.headers)

    def format_date(self, date: datetime) -> str:
        return date.astimezone().replace(microsecond=0).isoformat()
