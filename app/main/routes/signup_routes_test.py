from unittest import TestCase

import pytest
from fastapi.testclient import TestClient
from pymongo_inmemory import MongoClient

from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper
from app.main.config import make_app


@pytest.mark.integration
class SignUpRoutesTests(TestCase):
    """
    Sign Up Routes
    """

    @classmethod
    def setUpClass(cls) -> None:
        MongoHelper.connect(client_class=MongoClient)
        cls.client = TestClient(make_app())

    @classmethod
    def tearDownClass(cls) -> None:
        MongoHelper.disconnect()

    def setUp(self) -> None:
        account_collection = MongoHelper.get_collection("accounts")
        account_collection.delete_many({})

    def test_return_an_account_on_success(self):
        """
        Should return an account on success
        """

        response = self.client.post(
            "/api/signup",
            json={
                "name": "Raphael",
                "email": "rafaphcastro@gmail.com",
                "password": "123",
                "passwordConfirmation": "123",
            },
        )
        self.assertEqual(response.status_code, 200)
