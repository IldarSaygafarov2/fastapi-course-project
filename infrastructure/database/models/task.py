import datetime
import enum


from .base import Base, created_at, updated_at
from .mixins.int_id_pk import IntIdPxMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Enum as ENUM


class StatusEnum(enum.Enum):
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(Base, IntIdPxMixin):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[StatusEnum] = mapped_column(
        ENUM(StatusEnum), default=StatusEnum.IN_PROGRESS
    )
    finish_date: Mapped[datetime.datetime] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
