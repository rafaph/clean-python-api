from src.presentation.protocols.http import HttpRequest, HttpResponse
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request


class SignUpController:
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        if "name" not in httpRequest["body"]:
            return bad_request(MissingParamError("name"))

        if "email" not in httpRequest["body"]:
            return bad_request(MissingParamError("email"))
