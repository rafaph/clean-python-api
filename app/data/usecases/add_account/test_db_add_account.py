from dataclasses import dataclass
from unittest import TestCase, mock

from app.domain.usecases.add_account import AddAccountModel
from .db_add_account import DbAddAccount
from ...protocols.encrypter import Encrypter


@dataclass
class SutTypes:
    encrypter_stub: Encrypter
    sut: DbAddAccount


def make_sut():
    class EncrypterStub(Encrypter):
        def encrypt(self, value: str) -> str:
            return "hashed_password"

    encrypter_stub = EncrypterStub()
    sut = DbAddAccount(encrypter_stub)

    return SutTypes(sut=sut, encrypter_stub=encrypter_stub)


class DbAddAccountTests(TestCase):
    """
    DbAddAccount Usecase
    """

    def test_call_encrypter_with_correct_password(self):
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
