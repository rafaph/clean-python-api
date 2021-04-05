from unittest import TestCase

import pytest
from fastapi.testclient import TestClient

from app.main.config import make_app


@pytest.mark.integration
class SignUpRoutesTests(TestCase):
    """
    Sign Up Routes
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(make_app())

    def test_return_an_account_on_success(self):
        """
        Should return an account on success
        """

        response = self.client.post(
            "/api/signup",
            json={
                "data": {
                    "name": "Raphael",
                    "email": "rafaphcastro@gmail.com",
                    "password": "123",
                    "passwordConfirmation": "123",
                }
            },
        )
        self.assertEqual(response.status_code, 200)
