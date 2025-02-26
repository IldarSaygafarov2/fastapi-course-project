from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from .user import UserRepo
from .task import TaskRepo


@dataclass
class RequestsRepo:
    session: AsyncSession

    @property
    def users(self) -> UserRepo:
        return UserRepo(self.session)

    @property
    def tasks(self) -> TaskRepo:
        return TaskRepo(self.session)
