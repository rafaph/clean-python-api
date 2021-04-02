from typing import Any


class ValidationError(Exception):
    message = None

    def __init__(self, message):
        self.message = message

    def __eq__(self, instance):
        return instance.message == self.message


class SignUpController:
    def handle(self, httpRequest: Any) -> Any:
        return {"statusCode": 400, "body": ValidationError("Missing param: name")}
