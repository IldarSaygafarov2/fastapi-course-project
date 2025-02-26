from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_jwt_service, get_password_service, get_repo

from backend.core.services.password_service import PasswordService
from backend.core.services.jwt_service import JwtService
from infrastructure.database.repo.requests import RequestsRepo
from backend.core.interfaces.user import UserDTO, UserLoginDTO, UserRegisterDTO
from backend.core.interactors.register_user import RegisterUserInteractor
from backend.core.interactors.login_user import LoginUserInteractor


router = APIRouter(
    prefix=config.api_prefix.v1.auth,
    tags=["Auth"],
)


@router.post("/register")
async def register_user(
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    password_service: Annotated[PasswordService, Depends(get_password_service)],
    user_data: UserRegisterDTO,
) -> UserDTO | dict:
    interactor = RegisterUserInteractor(repo, password_service)
    return await interactor(user_data)


@router.post("/login")
async def login_user(
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    password_service: Annotated[PasswordService, Depends(get_password_service)],
    jwt_service: Annotated[JwtService, Depends(get_jwt_service)],
    login_user: UserLoginDTO,
):
    interactor = LoginUserInteractor(
        repo=repo, password_service=password_service, jwt_service=jwt_service
    )
    token = await interactor(login_user)
    return {"access_token": token, "token_type": "bearer"}
