import pytest
from eso_api.api.errors import (
    BadRequestError,
    ForbiddenResourceError,
    NoContentError,
    PayloadTooLargeError,
    ResourceNotFoundError,
    UnauthorizedError,
)
from eso_api.api.call import Call

testdata = [
    (204, NoContentError, "NoContentError"),
    (400, BadRequestError, "BadRequestError"),
    (401, UnauthorizedError, "UnauthorizedError"),
    (403, ForbiddenResourceError, "ForbiddenResourceError"),
    (404, ResourceNotFoundError, "ResourceNotFoundError"),
    (413, PayloadTooLargeError, "PayloadTooLargeError"),
]


@pytest.mark.parametrize("code,error,message", testdata)
def test_raise_errors(code, error, message):
    resp_dict = {"statusCode": code, "message": message}
    call = Call()

    with pytest.raises(error) as e:
        call.check_status(resp_dict)

    assert str(e.value) == message


def test_no_errors():
    resp_dict = {"statusCode": 200, "message": "OK"}
    call = Call()

    assert call.check_status(resp_dict) is None
    assert call.check_status([]) is None
