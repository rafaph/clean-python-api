from .db_add_account_protocols import (
    Encrypter,
    AddAccountModel,
    AccountModel,
    AddAccountRepository,
    AddAccount,
)


class DbAddAccount(AddAccount):
    def __init__(
        self, encrypter: Encrypter, add_account_repository: AddAccountRepository
    ):
        self._encrypter = encrypter
        self._add_account_repository = add_account_repository

    def add(self, account_data: AddAccountModel) -> AccountModel:
        return self._add_account_repository.add(
            account_data.copy(
                update={"password": self._encrypter.encrypt(account_data.password)}
            )
        )
