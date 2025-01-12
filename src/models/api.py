from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.services.dbService import db


# db = SQLAlchemy()


class Api(db.Model):
    __tablename__ = 'apis'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    api_name: Mapped[str] = mapped_column(String(255))
    api_key: Mapped[Optional[str]] = mapped_column(String(255))
    other: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='api使用时要用到的其他字段')

    def __init__(self, api_name: str, api_key: str, other: Optional[str] = None):
        self.api_name = api_name
        self.api_key = api_key
        self.other = other

    def __str__(self):
        return f'{self.api_name}, {self.api_key}, {self.other}'
