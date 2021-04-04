from unittest import TestCase

from pymongo_inmemory import MongoClient

from app.domain.usecases.add_account import AddAccountModel
from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper

from .account import AccountMongoRepository


def make_sut() -> AccountMongoRepository:
    return AccountMongoRepository()


class AccountMongoRepositoryTests(TestCase):
    """
    Account Mongo Repository
    """

    @classmethod
    def setUpClass(cls) -> None:
        MongoHelper.connect(client_class=MongoClient)

    @classmethod
    def tearDownClass(cls) -> None:
        MongoHelper.disconnect()

    def setUp(self) -> None:
        account_collection = MongoHelper.get_collection("accounts")
        account_collection.delete_many({})

    def test_returns_account_on_success(self):
        sut = make_sut()
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
