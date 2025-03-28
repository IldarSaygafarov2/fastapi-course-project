from passlib.context import CryptContext


class PasswordService:
    def __init__(self):
        self._password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self._password_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._password_context.verify(plain_password, hashed_password)
