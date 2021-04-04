from app.data.protocols.encrypter import Encrypter
import bcrypt


class BcryptAdapter(Encrypter):
    def __init__(self, rounds: int):
        self._rounds = rounds

    def encrypt(self, value: str) -> str:
        return bcrypt.hashpw(
            value.encode("utf-8"), bcrypt.gensalt(self._rounds)
        ).decode("utf-8")
