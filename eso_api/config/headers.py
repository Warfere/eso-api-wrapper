from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, AliasChoices
from pydantic_core import ValidationError


# pylint: disable=too-few-public-methods
class HeadersModel(BaseModel):
    uuid: UUID = Field(
        alias="X-B3-TraceId",
        validation_alias=AliasChoices("X-B3-TraceId", "uuid"),
        default=None,
    )
    api_key: Optional[str] = None

    def to_dict_without_none(self):
        return {
            k: v for k, v in self.model_dump(by_alias=True).items() if v is not None
        }


# pylint: disable=too-few-public-methods
class Headers:
    def __init__(self, api_key: str) -> None:
        """Creates HeadersModel for eso api call
        Args:
            api_key (str): api_key to authenticate. You can request it here:
            https://www.eso.lt/web/api-paslaugos-uzsakymas/307

        Raises:
            ValueError: Missing api_key
        """

        self.uuid = str(uuid4())
        self.api_key = api_key
        self.settings: dict[str, str] = {
            "api-key": self.api_key,
            "X-B3-TraceId": self.uuid,
        }

    def update(self, headers: dict[str, str]) -> dict[str, str] | ValidationError:
        """
        Updates headers for eso api
        Args:
        `HeadersModel` :
            uuid|X-B3-TraceId: UUID
            api_key: str
        """
        model = HeadersModel.model_validate(headers).to_dict_without_none()
        new_headers = {k: str(v) for k, v in model.items()}
        self.settings.update(new_headers)
        return self.settings
