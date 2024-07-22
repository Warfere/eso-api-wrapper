import requests
from typing import Dict
from .errors import *
from ..config.headers import Headers

DEV_HOST = "https://api-dev.eso.lt/"


class Call:
    def __init__(self) -> None:
        pass

    def get(self, url: str, headers: Headers) -> Dict:
        print(headers.settings)
        print(url)
        response = requests.get(DEV_HOST + url, headers=headers.settings)
        self.check_status(response)
        return response.json()

    def check_status(self, response: requests.Response) -> None:
        resp_dict = response.json()
        if type(resp_dict) == list:
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
