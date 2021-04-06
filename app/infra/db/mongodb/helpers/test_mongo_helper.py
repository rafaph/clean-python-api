from unittest import TestCase

import pytest
from pymongo_inmemory import MongoClient

from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper as sut


@pytest.mark.unit
class MongoHelperTests(TestCase):
    """
    Mongo Helper
    """

    @classmethod
    def setUpClass(cls) -> None:
        sut.connect(client_class=MongoClient, serverSelectionTimeoutMS=1)

    @classmethod
    def tearDownClass(cls) -> None:
        sut.disconnect()

    def test_reconnect_if_mongodb_is_down(self):
        """
        Should reconnect if mongodb is down
        """

        accounts_collection = sut.get_collection("accounts")
        self.assertTrue(bool(accounts_collection))
        sut.disconnect()

        accounts_collection = sut.get_collection("accounts")
        self.assertTrue(bool(accounts_collection))
