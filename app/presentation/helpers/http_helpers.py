from http import HTTPStatus
from typing import Any, Optional

from app.presentation.errors import ServerError
from app.presentation.protocols.http import HttpResponse


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(status=HTTPStatus.BAD_REQUEST, body=error)


def server_error(stack: Optional[str] = None) -> HttpResponse:
    return HttpResponse(
        status=HTTPStatus.INTERNAL_SERVER_ERROR, body=ServerError(stack)
    )


def ok(data: Any) -> HttpResponse:
    return HttpResponse(status=HTTPStatus.OK, body=data)
