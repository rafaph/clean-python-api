from src.presentation.errors import MissingParamError, InvalidParamError
from src.presentation.helpers import bad_request, server_error
from src.presentation.protocols import (
    Controller,
    EmailValidator,
    HttpRequest,
    HttpResponse,
)


class SignUpController(Controller):
    def __init__(self, email_validator: EmailValidator):
        self._email_validator = email_validator

    def handle(self, http_resquest: HttpRequest) -> HttpResponse:
        try:
            required_fields = ["name", "email", "password", "passwordConfirmation"]

            for field in required_fields:
                if field not in http_resquest["body"]:
                    return bad_request(MissingParamError(field))

            email, password, password_confirmation = (
                http_resquest["body"]["email"],
                http_resquest["body"]["password"],
                http_resquest["body"]["passwordConfirmation"],
            )
            if password != password_confirmation:
                return bad_request(InvalidParamError("passwordConfirmation"))

            is_valid = self._email_validator.is_valid(email)
            if not is_valid:
                return bad_request(InvalidParamError("email"))
        except:
            return server_error()
