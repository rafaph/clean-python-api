from dataclasses import dataclass
from unittest import TestCase, mock

from .db_add_account import DbAddAccount
from .db_add_account_protocols import (
    Encrypter,
    AddAccountModel,
    AccountModel,
    AddAccountRepository,
)


def make_encrypter() -> Encrypter:
    class EncrypterStub(Encrypter):
        def encrypt(self, value: str) -> str:
            return "hashed_password"

    return EncrypterStub()


def make_add_account_repository() -> AddAccountRepository:
    class AddAccountRepositoryStub(AddAccountRepository):
        def add(self, account_data: AddAccountModel) -> AccountModel:
            fake_account = AccountModel(
                id="valid_id",
                name="valid_name",
                email="valid_email@mail.com",
                password="hashed_password",
            )
            return fake_account

    return AddAccountRepositoryStub()


@dataclass
class SutTypes:
    encrypter_stub: Encrypter
    add_account_repository_stub: AddAccountRepository
    sut: DbAddAccount


def make_sut():
    encrypter_stub = make_encrypter()
    add_account_repository_stub = make_add_account_repository()
    sut = DbAddAccount(encrypter_stub, add_account_repository_stub)

    return SutTypes(
        sut=sut,
        encrypter_stub=encrypter_stub,
        add_account_repository_stub=add_account_repository_stub,
    )


class DbAddAccountTests(TestCase):
    """
    DbAddAccount Usecase
    """

    @staticmethod
    def test_call_encrypter_with_correct_password():
        """
        Should call Encrypter with correct password
        """

        sut_types = make_sut()
        sut, encrypter_stub = sut_types.sut, sut_types.encrypter_stub

        account_data = AddAccountModel(
            name="valid_name", email="valid_email@mail.com", password="valid_password"
        )

        with mock.patch.object(
            encrypter_stub, "encrypt", return_value="hashed_password"
        ) as encrypt_spy:
            sut.add(account_data)
            encrypt_spy.assert_called_once_with("valid_password")

    def test_throw_if_encrypter_throws(self):
        """
        Should throw if encrypter throws
        """

        def encrypt_mock(value: str):
            raise Exception()

        sut_types = make_sut()
        sut, encrypter_stub = sut_types.sut, sut_types.encrypter_stub

        account_data = AddAccountModel(
            name="valid_name", email="valid_email@mail.com", password="valid_password"
        )

        with mock.patch.object(
            encrypter_stub, "encrypt", encrypt_mock
        ), self.assertRaises(Exception):
            sut.add(account_data)

    @staticmethod
    def test_call_add_account_repository_with_correct_values():
        """
        Should call AddAccountRepository with correct values
        """

        sut_types = make_sut()
        sut, add_account_repository_stub = (
            sut_types.sut,
            sut_types.add_account_repository_stub,
        )

        account_data = AddAccountModel(
            name="valid_name", email="valid_email@mail.com", password="valid_password"
        )

        with mock.patch.object(add_account_repository_stub, "add") as add_spy:
            sut.add(account_data)
            add_spy.assert_called_once_with(
                AddAccountModel(
                    name="valid_name",
                    email="valid_email@mail.com",
                    password="hashed_password",
                )
            )
