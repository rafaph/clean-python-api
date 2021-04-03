from http import HTTPStatus

from app.presentation.controllers.signup.protocols import (
    AddAccount,
    AddAccountModel,
    Controller,
    EmailValidator,
    HttpRequest,
    HttpResponse,
)
from app.presentation.errors import InvalidParamError, MissingParamError
from app.presentation.helpers import bad_request, server_error, ok


class SignUpController(Controller):
    def __init__(self, email_validator: EmailValidator, add_account: AddAccount):
        self._email_validator = email_validator
        self._add_account = add_account

    def handle(self, http_resquest: HttpRequest) -> HttpResponse:
        try:
            required_fields = ["name", "email", "password", "passwordConfirmation"]

            for field in required_fields:
                if field not in http_resquest.body:
                    return bad_request(MissingParamError(field))

            email, password, password_confirmation = (
                http_resquest.body["email"],
                http_resquest.body["password"],
                http_resquest.body["passwordConfirmation"],
            )
            if password != password_confirmation:
                return bad_request(InvalidParamError("passwordConfirmation"))

            is_valid = self._email_validator.is_valid(email)
            if not is_valid:
                return bad_request(InvalidParamError("email"))

            account = self._add_account.add(
                AddAccountModel(
                    name=http_resquest.body["name"],
                    password=password,
                    email=email,
                )
            )
            return ok(data=account)
        except Exception:
            return server_error()
