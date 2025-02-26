from backend.core.interfaces.user import UserDTO, UserRegisterDTO
from backend.core.services.password_service import PasswordService
from infrastructure.database.repo.requests import RequestsRepo


class RegisterUserInteractor:
    def __init__(self, repo: RequestsRepo, password_service: PasswordService):
        self.repo = repo
        self.password_service = password_service

    async def __call__(self, register_user: UserRegisterDTO) -> UserDTO:
        exists = await self.repo.users.is_user_exists(register_user.username)

        if exists:
            return {"detail": "User already exists"}

        hash_password = self.password_service.hash_password(register_user.password)

        new_user = await self.repo.users.create_user(
            username=register_user.username,
            email=register_user.email,
            password=hash_password,
        )

        return UserDTO.model_validate(new_user, from_attributes=True)
