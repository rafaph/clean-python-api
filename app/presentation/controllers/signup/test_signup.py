from dataclasses import dataclass
from http import HTTPStatus
from unittest import TestCase, mock

import pytest

from app.presentation.controllers.signup.protocols import (
    AccountModel,
    AddAccount,
    AddAccountModel,
    EmailValidator,
    HttpRequest,
)
from app.presentation.errors import InvalidParamError, MissingParamError, ServerError

from .controller import SignUpController


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


@dataclass
class SutTypes:
    email_validator: EmailValidator
    sut: SignUpController
    add_account: AddAccount


def make_sut() -> SutTypes:
    email_validator_stub = make_email_validator()
    add_account_stub = make_add_account()
    sut = SignUpController(email_validator_stub, add_account_stub)

    return SutTypes(
        sut=sut, email_validator=email_validator_stub, add_account=add_account_stub
    )


@pytest.mark.unit
class SignUpControllerTests(TestCase):
    """
    SignUpConstroller tests
    """

    def test_return_400_no_name(self):
        """
        Should return status 400 if no name is provided
        """
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "email": "any_email@mail.com",
                "password": "any_password",
                "passwordConfirmation": "any_password",
            }
        )

        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(http_response.body, MissingParamError("name"))

    def test_return_400_no_email(self):
        """
        Should return status 400 if no email is provided
        """
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "name": "any_name",
                "password": "any_password",
                "passwordConfirmation": "any_password",
            }
        )

        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(http_response.body, MissingParamError("email"))

    def test_return_400_no_password(self):
        """
        Should return status 400 if no password is provided
        """
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@mail.com",
                "passwordConfirmation": "any_password",
            }
        )

        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(http_response.body, MissingParamError("password"))

    def test_return_400_no_password_confirmation(self):
        """
        Should return status 400 if no password confirmation is provided
        """
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@mail.com",
                "password": "any_password",
            }
        )

        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(http_response.body, MissingParamError("passwordConfirmation"))

    def test_return_400_password_confirmation_fails(self):
        """
        Should return status 400 if password confirmation fails
        """
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "name": "any_name",
                "email": "any_email@mail.com",
                "password": "invalid_passowrd",
                "passwordConfirmation": "any_passowrd",
            }
        )

        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
        self.assertEqual(http_response.body, InvalidParamError("passwordConfirmation"))

    def test_return_400_invalid_email(self):
        """
        Should return status 400 if an invalid email is provided
        """
        sut_types = make_sut()
        sut = sut_types.sut
        email_validator = sut_types.email_validator

        with mock.patch.object(email_validator, "is_valid", return_value=False):
            http_request = HttpRequest(
                body={
                    "name": "any_name",
                    "email": "invalid_email@mail.com",
                    "password": "any_password",
                    "passwordConfirmation": "any_password",
                }
            )

            http_response = sut.handle(http_request)
            self.assertEqual(http_response.status, HTTPStatus.BAD_REQUEST)
            self.assertEqual(http_response.body, InvalidParamError("email"))

    @staticmethod
    def test_call_email_validator_correct():
        """
        Should call EmailValidator with correct email
        """
        sut_types = make_sut()
        sut = sut_types.sut
        email_validator = sut_types.email_validator
        with mock.patch.object(email_validator, "is_valid") as spy_is_valid:
            http_request = HttpRequest(
                body={
                    "name": "any_name",
                    "email": "invalid_email@mail.com",
                    "password": "any_password",
                    "passwordConfirmation": "any_password",
                }
            )
            sut.handle(http_request)
            spy_is_valid.assert_called_with(http_request.body["email"])

    def test_return_500_email_validator_throws(self):
        """
        Should return status 500 if EmailValidator throws
        """

        def is_valid(email: str):
            raise Exception()

        sut_types = make_sut()
        sut = sut_types.sut
        email_validator = sut_types.email_validator

        with mock.patch.object(email_validator, "is_valid", is_valid):
            http_request = HttpRequest(
                body={
                    "name": "any_name",
                    "email": "any_email@mail.com",
                    "password": "any_password",
                    "passwordConfirmation": "any_password",
                }
            )
            http_response = sut.handle(http_request)
            self.assertEqual(http_response.status, HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertEqual(http_response.body, ServerError())

    @staticmethod
    def test_call_add_account_with_correct_values():
        """
        Should call AddAccount with correct values
        """
        sut_types = make_sut()
        sut = sut_types.sut
        add_account_stub = sut_types.add_account

        with mock.patch.object(add_account_stub, "add") as add_spy:
            http_request = HttpRequest(
                body={
                    "name": "any_name",
                    "email": "any_email@mail.com",
                    "password": "any_password",
                    "passwordConfirmation": "any_password",
                }
            )
            sut.handle(http_request)
            add_spy.assert_called_once_with(
                AddAccountModel(
                    name=http_request.body["name"],
                    email=http_request.body["email"],
                    password=http_request.body["password"],
                )
            )

    def test_return_500_add_account_throws(self):
        """
        Should return status 500 if AddAcount throws
        """

        def add():
            raise Exception()

        sut_types = make_sut()
        sut = sut_types.sut
        add_account_stub = sut_types.add_account

        with mock.patch.object(add_account_stub, "add", add):
            http_request = HttpRequest(
                body={
                    "name": "any_name",
                    "email": "any_email@mail.com",
                    "password": "any_password",
                    "passwordConfirmation": "any_password",
                }
            )
            http_response = sut.handle(http_request)
            self.assertEqual(http_response.status, HTTPStatus.INTERNAL_SERVER_ERROR)
            self.assertEqual(http_response.body, ServerError())

    def test_return_200_valid_data(self):
        sut = make_sut().sut
        http_request = HttpRequest(
            body={
                "name": "valid_name",
                "email": "valid_email@mail.com",
                "password": "valid_password",
                "passwordConfirmation": "valid_password",
            }
        )
        http_response = sut.handle(http_request)
        self.assertEqual(http_response.status, HTTPStatus.OK)
        self.assertEqual(
            http_response.body,
            AccountModel(
                id="valid_id",
                name="valid_name",
                email="valid_email@mail.com",
                password="valid_password",
            ),
        )
