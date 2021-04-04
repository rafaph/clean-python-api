from app.data.protocols.add_account_repository import AddAccountRepository
from app.domain.models.account import AccountModel
from app.domain.usecases.add_account import AddAccountModel

from ..helpers.mongo_helper import MongoHelper


class AccountMongoRepository(AddAccountRepository):
    def add(self, account_data: AddAccountModel) -> AccountModel:
        account_collection = MongoHelper.get_collection("accounts")
        result = account_collection.insert_one(account_data.dict())
        account = account_collection.find_one({"_id": result.inserted_id}).copy()
        account["id"] = str(account.pop("_id"))
        return AccountModel(**account)
