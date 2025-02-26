from .base import BaseRepo
from infrastructure.database.models import User

from sqlalchemy import insert, select, update, delete, exists


class UserRepo(BaseRepo):
    async def is_user_exists(self, username: str):
        stmt = select(exists().where(User.username == username))
        result = await self.session.execute(stmt)
        return result.scalar()

    async def create_user(self, username: str, email: str, password: str):
        stmt = (
            insert(User)
            .values(username=username, email=email, password=password)
            .returning(User)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str):
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
