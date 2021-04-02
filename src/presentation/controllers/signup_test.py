"""
SignUp Controller
"""
from typing import TypedDict

from src.presentation.controllers.signup import SignUpController
from src.presentation.errors import MissingParamError, InvalidParamError
from src.presentation.protocols.email_validator import EmailValidator


class SutTypes(TypedDict):
    email_validator: EmailValidator
    sut: SignUpController


def makeSut() -> SutTypes:
    class EmailValidatorStub(EmailValidator):
        def is_valid(self, email: str) -> bool:
            return True

    email_validator_stub = EmailValidatorStub()
    sut = SignUpController(email_validator_stub)

    return {"sut": sut, "email_validator": email_validator_stub}


def test_return_400_no_name():
    """
    Should return 400 if no name is provided
    """
    sut = makeSut()["sut"]
    http_request = {
        "body": {
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == MissingParamError("name")


def test_return_400_no_email():
    """
    Should return 400 if no email is provided
    """
    sut = makeSut()["sut"]
    http_request = {
        "body": {
            "name": "any_name",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == MissingParamError("email")


def test_return_400_no_password():
    """
    Should return 400 if no password is provided
    """
    sut = makeSut()["sut"]
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == MissingParamError("password")


def test_return_400_no_password_confirmation():
    """
    Should return 400 if no passwordConfirmation is provided
    """
    sut = makeSut()["sut"]
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == MissingParamError("passwordConfirmation")


def test_return_400_invalid_email(mocker):
    """
    Should return 400 if an invalid email is provided
    """
    sut_values = makeSut()
    sut = sut_values["sut"]
    email_validator = sut_values["email_validator"]
    mocker.patch.object(email_validator, "is_valid", return_value=False)
    http_request = {
        "body": {
            "name": "any_name",
            "email": "invalid_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == InvalidParamError("email")


def test_call_email_validator_correct(mocker):
    """
    Should call EmailValidator with correct email
    """
    sut_values = makeSut()
    sut = sut_values["sut"]
    email_validator = sut_values["email_validator"]
    spy = mocker.patch.object(email_validator, "is_valid")
    http_request = {
        "body": {
            "name": "any_name",
            "email": "invalid_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    sut.handle(http_request)
    spy.assert_called_with(http_request["body"]["email"])
