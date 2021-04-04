from typing import Optional

from pymongo import MongoClient
from pymongo.collection import Collection


class MongoHelper:
    client: MongoClient
    db: str = "clean-python-api"

    @classmethod
    def connect(
        cls,
        *,
        url: Optional[str] = None,
        client_class: Optional = MongoClient,
    ) -> None:
        cls.client = client_class(url)

    @classmethod
    def disconnect(cls) -> None:
        cls.client.close()

    @classmethod
    def get_collection(cls, name: str) -> Collection:
        return cls.client[cls.db][name]
