from typing import Any
from dataclasses import dataclass


class ValidationError(Exception):
    message = None

    def __init__(self, message):
        self.message = message

    def __eq__(self, instance):
        return instance.message == self.message


@dataclass
class HttpResponse:
    status: int
    body: Any


@dataclass
class HttpRequest:
    body: Any


class SignUpController:
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        if "name" not in httpRequest.body:
            return HttpResponse(status=400, body=ValidationError("Missing param: name"))

        if "email" not in httpRequest.body:
            return HttpResponse(
                status=400, body=ValidationError("Missing param: email")
            )
