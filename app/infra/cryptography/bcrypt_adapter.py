from app.data.protocols.encrypter import Encrypter
import bcrypt


def hashpw(value: str, rounds: int) -> str:
    return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt(rounds)).decode("utf-8")


class BcryptAdapter(Encrypter):
    def __init__(self, rounds: int):
        self._rounds = rounds

    def encrypt(self, value: str) -> str:
        return hashpw(value, self._rounds)
