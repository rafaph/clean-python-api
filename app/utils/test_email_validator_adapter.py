from unittest import TestCase

from app.utils.email_validator import EmailValidatorAdapter


class EmailValidatorAdapterTests(TestCase):
    """
    EmailValidator Adapter
    """

    def test_return_false_if_validator_returns_false(self):
        """
        Should return false if validator returns false
        """
        sut = EmailValidatorAdapter()
        is_valid = sut.is_valid("invalid_email@mail.com")
        self.assertFalse(is_valid)
