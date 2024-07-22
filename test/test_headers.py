from pydantic_core import ValidationError
from eso_api import Headers
from pytest import raises


def test_headers_uuid():
    new_header = Headers(api_key="")
    assert type(new_header.uuid) == str


def test_headers_api_key():
    new_header = Headers(api_key="my_key")
    assert new_header.api_key == "my_key"


def test_headers_update_validation():
    headers = Headers(api_key="")
    with raises(ValidationError):
        headers.update({"uuid": "new_headers"})


def test_headers_update():
    headers = Headers(api_key="")
    headers.update({"uuid": "f47ac10b-58cc-4372-a567-0e02b2c3d479"})
    assert headers.settings["X-B3-TraceId"] == "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    headers.update({"X-B3-TraceId": "f47ac10b-58cc-4372-a567-0e02b2c3d420"})
    assert headers.settings["X-B3-TraceId"] == "f47ac10b-58cc-4372-a567-0e02b2c3d420"
    headers.update({"api_key": "0e02b2c3d420"})
    assert headers.settings["api_key"] == "0e02b2c3d420"
    assert headers.settings["X-B3-TraceId"] == "f47ac10b-58cc-4372-a567-0e02b2c3d420"
