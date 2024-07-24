class EsoError(Exception):
    """
    EsoError wrapper for error message formatting

    """

    def __init__(self, resp_dict) -> None:
        """
        Constructs message from response and calls Exception
        Args:
            resp_dict (Dict):
                {
                    "statusCode": int,
                    "message": "string"
                }
        """
        super().__init__(resp_dict["message"])


class NoContentError(EsoError):
    """
    No Content 204 The request has succeeded,
    but no data found according to the given parameters.
     Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """


class BadRequestError(EsoError):
    """Bad Request 400 The server cannot or will
    not process the request due to a client error
    (e.g. malformed request syntax:mandatory parameters,
    headers, etc. must be specified).
    Constructs message from response and calls Exception

    Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """


class UnauthorizedError(EsoError):
    """
    Unauthorized 401 The authentication credentials are
    incorrect. The user may repeat the request with a
    new or replaced Authorization header field.
    "Constructs message from response and calls Exception

    Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """


class ForbiddenResourceError(EsoError):
    """
    Forbidden 403 Client doesn’t have
    the necessary privilege to access
    the resource; or Exceeding quota limits.
    Error message text: “Out of call volume
    quota. Quota will be replenished in {dd.hh:mm:ss}”
    Constructs message from response and calls Exception

    Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """


class ResourceNotFoundError(EsoError):
    """
    Not Found 404 The server cannot find the requested resource
    Constructs message from response and calls Exception

    Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """


class PayloadTooLargeError(EsoError):
    """
    Payload Too Large 413 Exceeding response
    size limits. Error message text:
    “Maximum allowed size for the response is … bytes
    (… MB). This response has size of … bytes.”
    Constructs message from response and calls Exception

    Args:
        resp_dict (Dict):
            {
                "statusCode": int,
                "message": "string"
            }
    """
