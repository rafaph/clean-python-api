from unittest import TestCase

from pymongo_inmemory import MongoClient

from app.domain.usecases.add_account import AddAccountModel

from ..helpers.mongo_helper import MongoHelper
from .account import AccountMongoRepository


class AccountMongoRepositoryTests(TestCase):
    """
    Account Mongo Repository
    """

    def setUp(self) -> None:
        MongoHelper.connect(client_class=MongoClient)

    def tearDown(self) -> None:
        MongoHelper.disconnect()

    def test_returns_account_on_success(self):
        sut = AccountMongoRepository()
        account = sut.add(
            AddAccountModel(
                name="any_name", email="any_email@mail.com", password="any_password"
            )
        )
        self.assertTrue(bool(account))
        self.assertTrue(bool(account.id))
        self.assertEqual(account.name, "any_name")
        self.assertEqual(account.email, "any_email@mail.com")
        self.assertEqual(account.password, "any_password")
