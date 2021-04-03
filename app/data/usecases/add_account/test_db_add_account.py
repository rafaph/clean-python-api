from dataclasses import dataclass
from unittest import TestCase, mock

from .db_add_account import DbAddAccount
from .db_add_account_protocols import Encrypter, AddAccountModel


def make_encrypter() -> Encrypter:
    class EncrypterStub(Encrypter):
        def encrypt(self, value: str) -> str:
            return "hashed_password"

    return EncrypterStub()


@dataclass
class SutTypes:
    encrypter_stub: Encrypter
    sut: DbAddAccount


def make_sut():
    encrypter_stub = make_encrypter()
    sut = DbAddAccount(encrypter_stub)

    return SutTypes(sut=sut, encrypter_stub=encrypter_stub)


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

        with mock.patch.object(encrypter_stub, "encrypt") as encrypt_spy:
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
