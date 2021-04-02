"""
SignUp Controller
"""
from typing import TypedDict

from app.presentation.controllers.signup.controller import SignUpController
from app.presentation.controllers.signup.protocols import (
    EmailValidator,
    AccountModel,
    AddAccountModel,
    AddAccount,
)
from app.presentation.errors import MissingParamError, InvalidParamError, ServerError


def make_email_validator() -> EmailValidator:
    class EmailValidatorStub(EmailValidator):
        def is_valid(self, email: str) -> bool:
            return True

    return EmailValidatorStub()


def make_add_account() -> AddAccount:
    class AddAccountStub(AddAccount):
        def add(self, account: AddAccountModel) -> AccountModel:
            return AccountModel(
                id="valid_id",
                name="valid_name",
                email="valid_email@mail.com",
                password="valid_password",
            )

    return AddAccountStub()


class SutTypes(TypedDict):
    email_validator: EmailValidator
    sut: SignUpController
    add_account: AddAccount


def make_sut() -> SutTypes:
    email_validator_stub = make_email_validator()
    add_account_stub = make_add_account()
    sut = SignUpController(email_validator_stub, add_account_stub)

    return {
        "sut": sut,
        "email_validator": email_validator_stub,
        "add_account": add_account_stub,
    }


def test_return_400_no_name():
    """
    Should return 400 if no name is provided
    """
    sut = make_sut()["sut"]
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
    sut = make_sut()["sut"]
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
    sut = make_sut()["sut"]
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


def test_return_400_password_confirmation_fail():
    """
    Should return 400 if password confirmation fails
    """
    sut = make_sut()["sut"]
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "invalid_passowrd",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 400
    assert http_response["body"] == InvalidParamError("passwordConfirmation")


def test_return_400_no_password_confirmation():
    """
    Should return 400 if no passwordConfirmation is provided
    """
    sut = make_sut()["sut"]
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
    sut_values = make_sut()
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
    sut_values = make_sut()
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


def test_return_500_email_validator_throws(mocker):
    """
    Should return 500 if EmailValidator throws
    """

    def custom_is_valid(email: str):
        raise Exception()

    sut_items = make_sut()
    sut = sut_items["sut"]
    email_validator = sut_items["email_validator"]
    mocker.patch.object(email_validator, "is_valid", custom_is_valid)
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 500
    assert http_response["body"] == ServerError()


def test_call_add_acount_correct_values(mocker):
    """
    Should call AddAccount with correct values
    """
    sut_values = make_sut()
    sut = sut_values["sut"]
    add_account_stub = sut_values["add_account"]
    add_spy = mocker.patch.object(add_account_stub, "add")
    http_request = {
        "body": {
            "name": "any_name",
            "email": "invalid_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    sut.handle(http_request)
    add_spy.assert_called_once_with(
        {
            "name": "any_name",
            "email": "invalid_email@mail.com",
            "password": "any_password",
        }
    )


def test_return_500_add_account_throws(mocker):
    """
    Should return 500 if AddAccount throws
    """

    def custom_add():
        raise Exception()

    sut_items = make_sut()
    sut = sut_items["sut"]
    add_account_stub = sut_items["add_account"]
    mocker.patch.object(add_account_stub, "add", custom_add)
    http_request = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    http_response = sut.handle(http_request)
    assert http_response["status_code"] == 500
    assert http_response["body"] == ServerError()
