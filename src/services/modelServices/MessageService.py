#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :MessageService.py
# @Time      :2025/1/13 17:10
# @Author    :Shao YiHan
from sqlalchemy import asc

from src.services.dbService import db
from src.models.message import Message
from sqlalchemy.exc import SQLAlchemyError


class MessageService:

    @staticmethod
    def get_message_by_id(message_id: int) -> Message:
        """
        根据消息ID获取消息。
        :param message_id: 消息ID
        :return: Message对象或None
        """
        try:
            return Message.query.filter_by(id=message_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_messages_by_conversation_id(conversation_id: int) -> list[Message]:
        """
        获取指定会话的所有消息。
        :param conversation_id: 会话ID
        :return: 消息对象列表
        """
        try:
            return Message.query.filter_by(conversation_id=conversation_id).order_by(Message.id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def create_message(conversation_id: int, sender: str, message_content: str) -> Message:
        """
        创建一个新消息。
        :param conversation_id: 会话ID
        :param sender: 发送者（user 或 system）
        :param message_content: 消息内容
        :return: 新创建的Message对象
        """
        new_message = Message(conversation_id=conversation_id, sender=sender, message_content=message_content)
        try:
            db.session.add(new_message)
            db.session.commit()
            return new_message
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_message(message_id: int) -> bool:
        """
        根据消息ID删除消息。
        :param message_id: 消息ID
        :return: 删除成功返回True，否则返回False
        """
        message = MessageService.get_message_by_id(message_id)
        if not message:
            raise ValueError("消息未找到")

        try:
            db.session.delete(message)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_message(message_id: int, **kwargs) -> Message:
        """
        根据消息ID更新消息信息。
        :param message_id: 消息ID
        :param kwargs: 要更新的字段及其值
        :return: 更新后的Message对象
        """
        message = MessageService.get_message_by_id(message_id)
        if not message:
            raise ValueError("消息未找到")

        try:
            for key, value in kwargs.items():
                if hasattr(message, key):
                    setattr(message, key, value)

            db.session.commit()
            return message
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e


if __name__ == '__main__':
    code = 0
