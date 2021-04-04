from typing import Any, Dict, Optional

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

    @staticmethod
    def map(item: Dict[str, Any]) -> Dict[str, Any]:
        new_item = item.copy()
        new_item["id"] = str(new_item.pop("_id"))
        return new_item
