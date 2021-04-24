import unittest

import pytest
from pymongo_inmemory import MongoClient

from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper
from app.infra.db.mongodb.log_repository.log import LogErrorMongoRepository


@pytest.mark.unit
class LogMongoRepositoryTests(unittest.TestCase):
    """
    Log Mongo Repository
    """

    @classmethod
    def setUpClass(cls) -> None:
        MongoHelper.connect(client_class=MongoClient)
        cls.errors_collection = MongoHelper.get_collection("errors")

    @classmethod
    def tearDownClass(cls) -> None:
        MongoHelper.disconnect()

    def setUp(self) -> None:
        self.errors_collection.delete_many({})

    def test_create_error_log_on_success(self):
        """
        Should create an error log on success
        """
        sut = LogErrorMongoRepository()
        sut.log_error("any_error")
        count = self.errors_collection.count_documents({})
        self.assertEqual(count, 1)
