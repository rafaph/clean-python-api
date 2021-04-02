"""
SignUp Controller
"""
from src.presentation.controllers.signup import (
    SignUpController,
    ValidationError,
    HttpRequest,
)


def test_return_400_no_name():
    """
    Should return 400 if no name is provided
    """
    sut = SignUpController()
    httpRequest = HttpRequest(
        body={
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    )
    httpResponse = sut.handle(httpRequest)
    assert httpResponse.status == 400
    assert httpResponse.body == ValidationError("Missing param: name")


def test_return_400_no_email():
    """
    Should return 400 if no email is provided
    """
    sut = SignUpController()
    httpRequest = HttpRequest(
        body={
            "name": "any_name",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    )
    httpResponse = sut.handle(httpRequest)
    assert httpResponse.status == 400
    assert httpResponse.body == ValidationError("Missing param: email")
