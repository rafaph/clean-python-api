class ValidationError(Exception):
    message = None

    def __init__(self, message):
        self.message = message

    def __eq__(self, instance):
        return instance.message == self.message