from src.presentation.protocols.http import HttpRequest, HttpResponse
from src.presentation.errors import MissingParamError


class SignUpController:
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        if "name" not in httpRequest["body"]:
            return HttpResponse(status_code=400, body=MissingParamError("name"))

        if "email" not in httpRequest["body"]:
            return HttpResponse(status_code=400, body=MissingParamError("email"))
