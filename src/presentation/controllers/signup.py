from src.presentation.protocols.http import HttpRequest, HttpResponse
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request


class SignUpController:
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        required_fields = ["name", "email", "password"]

        for field in required_fields:
            if field not in httpRequest["body"]:
                return bad_request(MissingParamError(field))
