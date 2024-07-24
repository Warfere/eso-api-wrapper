from typing import Dict, List
import requests
from eso_api.api.errors import (
    BadRequestError,
    ForbiddenResourceError,
    NoContentError,
    PayloadTooLargeError,
    ResourceNotFoundError,
    UnauthorizedError,
    EsoError,
)
from ..config.headers import Headers

DEV_HOST = "https://api-dev.eso.lt/"


class Call:
    def __init__(self) -> None:
        pass

    def get(self, url: str, headers: Headers) -> List:
        try:
            response = requests.get(
                DEV_HOST + url, headers=headers.settings, timeout=10
            ).json()
        except requests.Timeout as e:
            return [{"error": e}]
        except EsoError as e:
            return [{"error": e}]
        self.check_status(response)
        return [response]

    def check_status(self, resp_dict: Dict | List) -> None:
        if isinstance(resp_dict, list):
            return
        status = resp_dict.get("statusCode")

        if status == 204:
            raise NoContentError(resp_dict)
        if status == 400:
            raise BadRequestError(resp_dict)
        if status == 401:
            raise UnauthorizedError(resp_dict)
        if status == 403:
            raise ForbiddenResourceError(resp_dict)
        if status == 404:
            raise ResourceNotFoundError(resp_dict)
        if status == 413:
            raise PayloadTooLargeError(resp_dict)
