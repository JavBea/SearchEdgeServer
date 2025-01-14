import datetime
from typing import Optional

from sqlalchemy import ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column

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

    # user: Mapped['User'] = relationship('User', back_populates='conversations')
