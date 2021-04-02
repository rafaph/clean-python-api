"""
SignUp Controller
"""
from src.presentation.controllers.signup import SignUpController
from src.presentation.errors import MissingParamError


def makeSut() -> SignUpController:
    return SignUpController()


def test_return_400_no_name():
    """
    Should return 400 if no name is provided
    """
    sut = makeSut()
    httpRequest = {
        "body": {
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    httpResponse = sut.handle(httpRequest)
    assert httpResponse["status_code"] == 400
    assert httpResponse["body"] == MissingParamError("name")


def test_return_400_no_email():
    """
    Should return 400 if no email is provided
    """
    sut = makeSut()
    httpRequest = {
        "body": {
            "name": "any_name",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    httpResponse = sut.handle(httpRequest)
    assert httpResponse["status_code"] == 400
    assert httpResponse["body"] == MissingParamError("email")


def test_return_400_no_password():
    """
    Should return 400 if no password is provided
    """
    sut = makeSut()
    httpRequest = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "passwordConfirmation": "any_password",
        }
    }
    httpResponse = sut.handle(httpRequest)
    assert httpResponse["status_code"] == 400
    assert httpResponse["body"] == MissingParamError("password")


def test_return_400_no_password_confirmation():
    """
    Should return 400 if no passwordConfirmation is provided
    """
    sut = makeSut()
    httpRequest = {
        "body": {
            "name": "any_name",
            "email": "any_email@mail.com",
            "password": "any_password",
        }
    }
    httpResponse = sut.handle(httpRequest)
    assert httpResponse["status_code"] == 400
    assert httpResponse["body"] == MissingParamError("passwordConfirmation")
