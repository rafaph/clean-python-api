from typing import Any, Dict, Optional

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure


class MongoHelper:
    client: Optional[MongoClient] = None
    db: str = "clean-python-api"
    _url: Optional = None
    _client_class: Optional = None
    _kwargs = Optional = None

    @classmethod
    def connect(
        cls,
        *,
        url=None,
        client_class=MongoClient,
        **kwargs,
    ) -> None:
        cls._url = url
        cls._client_class = client_class
        cls._kwargs = kwargs
        cls.client = client_class(url, **kwargs)

    @classmethod
    def disconnect(cls) -> None:
        cls.client.close()
        cls.client = None

    @classmethod
    def is_connected(cls):
        if cls.client:
            try:
                cls.client.admin.command("ismaster")
                return True
            except ConnectionFailure:
                pass
        return False

    @classmethod
    def get_collection(cls, name: str) -> Collection:
        if not cls.is_connected():
            cls.connect(url=cls._url, client_class=cls._client_class, **cls._kwargs)
        return cls.client[cls.db][name]

    @staticmethod
    def map(item: Dict[str, Any]) -> Dict[str, Any]:
        new_item = item.copy()
        new_item["id"] = str(new_item.pop("_id"))
        return new_item
