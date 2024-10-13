class CustomError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidEmailError(CustomError):
    def __init__(self) -> None:
        super().__init__('Invalid email format')


class CipherKeyNotFoundError(CustomError):
    def __init__(self) -> None:
        super().__init__('Cipher key not found. Please create or set a key before encryption/decryption.')


class InvalidCipherKeyError(CustomError):
    def __init__(self) -> None:
        super().__init__('Invalid cipher key')
