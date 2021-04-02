from src.presentation.errors import MissingParamError, InvalidParamError
from src.presentation.helpers import bad_request
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.email_validator import EmailValidator
from src.presentation.protocols.http import HttpRequest, HttpResponse


class SignUpController(Controller):
    def __init__(self, email_validator: EmailValidator):
        self._email_validator = email_validator

    def handle(self, http_resquest: HttpRequest) -> HttpResponse:
        required_fields = ["name", "email", "password", "passwordConfirmation"]

        for field in required_fields:
            if field not in http_resquest["body"]:
                return bad_request(MissingParamError(field))

        is_valid = self._email_validator.is_valid(http_resquest["body"]["email"])
        if not is_valid:
            return bad_request(InvalidParamError("email"))
