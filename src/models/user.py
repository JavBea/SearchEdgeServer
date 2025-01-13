from typing import Optional

from sqlalchemy import Enum, Integer, String, text
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.services.dbService import db


class User(db.Model):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(ENUM('available', 'banned'), server_default=text("'banned'"))
    role: Mapped[str] = mapped_column(Enum('user', 'admin'), server_default=text("'user'"))
    user_name: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(255))
