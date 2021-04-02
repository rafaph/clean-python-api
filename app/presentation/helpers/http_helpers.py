from app.presentation.errors import ServerError
from app.presentation.protocols.http import HttpResponse


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=400, body=error)


def server_error() -> HttpResponse:
    return HttpResponse(status_code=500, body=ServerError())