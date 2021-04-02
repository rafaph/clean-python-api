from src.presentation.protocols.http import HttpRequest, HttpResponse
from src.presentation.errors.validation import ValidationError


class SignUpController:
    def handle(self, httpRequest: HttpRequest) -> HttpResponse:
        if "name" not in httpRequest["body"]:
            return HttpResponse(
                status_code=400, body=ValidationError("Missing param: name")
            )

        if "email" not in httpRequest["body"]:
            return HttpResponse(
                status_code=400, body=ValidationError("Missing param: email")
            )
