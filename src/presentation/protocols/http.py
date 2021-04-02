from typing import TypedDict, Any


class HttpResponse(TypedDict):
    status_code: int
    body: Any


class HttpRequest(TypedDict, total=False):
    body: Any
