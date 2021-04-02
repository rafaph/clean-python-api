"""
SignUp Controller
"""
from src.presentation.controllers.signup import SignUpController, ValidationError


def test_return_400():
    """
    Should return 400 if no name is provided
    """
    sut = SignUpController()
    httpRequest = {
        "body": {
            "email": "any_email@mail.com",
            "password": "any_password",
            "passwordConfirmation": "any_password",
        }
    }
    httpResponse = sut.handle(httpRequest)
    assert httpResponse["statusCode"] == 400
    assert httpResponse["body"] == ValidationError("Missing param: name")
