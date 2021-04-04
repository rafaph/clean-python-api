from unittest import TestCase, mock

import pytest

from .bcrypt_adapter import BcryptAdapter


@pytest.mark.unit
class BcryptAdapterTests(TestCase):
    """
    Bcrypt Adapter
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.hashpw_patcher = mock.patch("app.infra.cryptography.bcrypt_adapter.hashpw")

    def setUp(self) -> None:
        self.hashpw_stub = self.hashpw_patcher.start()
        self.hashpw_stub.return_value = "hashed_value"

    def tearDown(self) -> None:
        self.hashpw_patcher.stop()

    def test_call_bcrypt_with_correct_values(self):
        """
        Should call bcrypt with correct values
        """
        self.hashpw_patcher.stop()

        with mock.patch(
            "app.infra.cryptography.bcrypt_adapter.bcrypt.hashpw",
            return_value=b"hashed_value",
        ) as hashpw_spy:
            rounds = 12
            sut = BcryptAdapter(rounds)
            value = "any_value"
            sut.encrypt(value)
            hashpw_spy.assert_called_once_with(value.encode("utf-8"), mock.ANY)

    def test_call_hashpw_with_correct_values(self):
        """
        Should call hashpw with correct values
        """
        rounds = 12
        sut = BcryptAdapter(rounds)
        value = "any_value"
        sut.encrypt(value)
        self.hashpw_stub.assert_called_once_with(value, rounds)
