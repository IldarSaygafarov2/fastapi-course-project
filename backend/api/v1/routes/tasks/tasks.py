from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.config import config
from backend.app.dependencies import get_repo
from infrastructure.database.repo.requests import RequestsRepo
from backend.api.infrastructure.security.auth import get_current_user
from infrastructure.database.models import User
from backend.core.interfaces.task import TaskDTO, TaskCreateDTO, TaskUpdateDTO

router = APIRouter(
    prefix=config.api_prefix.v1.tasks,
    tags=["Tasks"],
)


@router.get("/")
async def get_tasks(
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    user: Annotated[User, Depends(get_current_user)],
) -> list[TaskDTO] | dict:
    tasks = await repo.tasks.get_user_tasks(user_id=user.id)
    return tasks


@router.post("/")
async def create_task(
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    user: Annotated[User, Depends(get_current_user)],
    task_data: TaskCreateDTO,
) -> TaskDTO:
    task = await repo.tasks.add_task(
        user_id=user.id,
        name=task_data.name,
        description=task_data.description,
        status=task_data.status.value,
        # finish_date=task_data.finish_date,
    )
    return task


@router.get("/{task_id}")
async def get_task_detail(
    task_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    user: Annotated[User, Depends(get_current_user)],
):
    task = await repo.tasks.get_task_detail(user_id=user.id, task_id=task_id)
    return task


@router.patch("/{task_id}")
async def update_task(
    task_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    user: Annotated[User, Depends(get_current_user)],
    task_data: TaskUpdateDTO,
):
    data = task_data.model_dump(exclude_none=True)

    updated = await repo.tasks.update_task(
        task_id=task_id,
        user_id=user.id,
        **data,
    )
    now = datetime.now()
    if updated.status.value == "done":
        await repo.tasks.update_task(
            task_id=task_id,
            user_id=user.id,
            finish_date=now,
        )
    return updated


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    repo: Annotated[RequestsRepo, Depends(get_repo)],
    user: Annotated[User, Depends(get_current_user)],
):
    deleted = await repo.tasks.delete_task(task_id=task_id, user_id=user.id)
    return {"deleted": deleted}
