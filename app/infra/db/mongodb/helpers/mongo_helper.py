from typing import Optional

from pymongo import MongoClient


class MongoHelper:
    client: MongoClient

    @classmethod
    def connect(
        cls,
        *,
        host: Optional[str] = None,
        port: Optional[int] = None,
        client_class: Optional = MongoClient,
    ) -> None:
        cls.client = client_class(host=host, port=port)

    @classmethod
    def disconnect(cls) -> None:
        cls.client.close()
