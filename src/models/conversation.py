from typing import List, Optional

from sqlalchemy import Enum, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

from src.models.user import User
from src.services.dbService import db


class Conversation(db.Model):
    __tablename__ = 'conversations'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='RESTRICT', onupdate='RESTRICT',
                             name='conversations_ibfk_1'),
        Index('user_id', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    user: Mapped['User'] = relationship('Users', back_populates='conversations')
