from typing import List, Optional

from sqlalchemy import Enum, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

from src.models.conversation import Conversation
from src.services.dbService import db


class Message(db.Model):
    __tablename__ = 'conversation_messages'
    __table_args__ = (
        ForeignKeyConstraint(['conversation_id'], ['conversations.id'], name='conversation_messages_ibfk_1'),
        Index('conversation_id', 'conversation_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    conversation_id: Mapped[int] = mapped_column(Integer)
    sender: Mapped[str] = mapped_column(Enum('user', 'system'))
    message_content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    # conversation: Mapped['Conversation'] = relationship('Conversations', back_populates='conversation_messages')
