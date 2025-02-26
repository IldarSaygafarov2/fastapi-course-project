from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IntIdPxMixin


class User(Base, IntIdPxMixin):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
