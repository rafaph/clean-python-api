from datetime import datetime

from app.data.protocols.log_error_repository import LogErrorRepository
from app.infra.db.mongodb.helpers.mongo_helper import MongoHelper


class LogErrorMongoRepository(LogErrorRepository):
    def log_error(self, stack: str) -> None:
        error_collection = MongoHelper.get_collection("errors")
        error_collection.insert_one({"stack": stack, "date": datetime.now()})
