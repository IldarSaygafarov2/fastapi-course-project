from infrastructure.database.repo.requests import RequestsRepo
from backend.core.services.password_service import PasswordService
from backend.core.services.jwt_service import JwtService
from backend.core.interfaces.user import UserLoginDTO


class LoginUserInteractor:
    def __init__(
        self,
        repo: RequestsRepo,
        password_service: PasswordService,
        jwt_service: JwtService,
    ):
        self.repo = repo
        self.password_service = password_service
        self.jwt_service = jwt_service

    async def __call__(self, login_user: UserLoginDTO):
        user = await self.repo.users.get_by_email(login_user.email)

        if not user or not self.password_service.verify_password(
            login_user.password, user.password
        ):
            return {"detail": "Incorrect email or password"}

        access_token = self.jwt_service.create_access_token({"sub": user.email})
        return access_token
