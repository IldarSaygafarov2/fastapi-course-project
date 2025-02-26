import datetime
from typing import Optional
from .base import BaseRepo

from infrastructure.database.models.task import Task


from sqlalchemy import select, insert, update, delete


class TaskRepo(BaseRepo):
    async def add_task(
        self,
        name: str,
        description: Optional[str],
        user_id: int,
        finish_date: Optional[datetime.datetime] = None,
    ):
        stmt = (
            insert(Task)
            .values(
                name=name,
                description=description,
                finish_date=finish_date,
                user_id=user_id,
            )
            .returning(Task)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_user_tasks(self, user_id: int):
        stmt = select(Task).where(Task.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_task_detail(self, user_id: int, task_id: int):
        stmt = select(Task).where(Task.user_id == user_id, Task.id == task_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_task(self, task_id: int, user_id: int, **data):
        stmt = (
            update(Task)
            .where(Task.id == task_id, Task.user_id == user_id)
            .values(**data)
            .returning(Task)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def delete_task(self, task_id: int, user_id: int):
        stmt = delete(Task).where(Task.id == task_id, Task.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount
