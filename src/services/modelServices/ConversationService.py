#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ConversationService.py
# @Time      :2025/1/13 17:09
# @Author    :Shao YiHan
from typing import Optional

from src.services.dbService import db
from src.models.conversation import Conversation
from sqlalchemy.exc import SQLAlchemyError


class ConversationService:

    @staticmethod
    def get_conversation_by_id(conversation_id: int) -> Conversation:
        """
        根据会话ID获取会话。
        :param conversation_id: 会话ID
        :return: Conversation对象或None
        """
        try:
            return Conversation.query.filter_by(id=conversation_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_all_conversations_by_user_id(user_id: int) -> Optional[list[Conversation]]:
        """
        获取指定用户的所有会话。
        :param user_id: 用户ID
        :return: 会话对象列表
        """
        try:
            # 检查user_id是否存在
            from src.services.modelServices.UserService import UserService

            if UserService.get_user_by_id(user_id) is None:
                return None

            return Conversation.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def create_conversation(user_id: int, title: str):
        """
        创建一个新会话。
        :param user_id: 用户ID
        :param title: 会话标题
        :return: 新创建的Conversation对象, 创建会话响应码code：code=3001(创建会话成功),code=3002(创建会话失败)
        """

        # 检查user_id是否存在
        from src.services.modelServices.UserService import UserService

        if UserService.get_user_by_id(user_id) is None:
            return None, "3002"

        new_conversation = Conversation(user_id=user_id, title=title)
        try:
            db.session.add(new_conversation)
            db.session.commit()
            return new_conversation, "3001"
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def check_conversation(conversation_id: int):
        """
        根据id检查会话是否存在
        :param conversation_id: 检索的会话id
        :return: 返回布尔值
        """
        conversation = ConversationService.get_conversation_by_id(conversation_id)
        if conversation is None:
            return False
        return True

    @staticmethod
    def update_conversation(conversation_id: int, **kwargs):
        """
        根据会话ID更新会话信息。
        :param conversation_id: 会话ID
        :param kwargs: 要更新的字段及其值
        :return: 更新后的Conversation对象, 更新响应码code：code=4001(会话更新成功),code=4002(会话更新失败)
        """
        conversation = ConversationService.get_conversation_by_id(conversation_id)

        if not conversation:
            return None, "4002"

        try:
            for key, value in kwargs.items():
                if hasattr(conversation, key):
                    setattr(conversation, key, value)

            db.session.commit()
            return conversation, "4001"
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_conversation(conversation_id: int) -> bool:
        """
        根据会话ID删除会话。
        :param conversation_id: 会话ID
        :return: 删除成功返回True，否则返回False
        """
        conversation = ConversationService.get_conversation_by_id(conversation_id)
        if not conversation:
            raise ValueError("会话未找到")

        try:
            db.session.delete(conversation)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e


if __name__ == '__main__':
    code = 0
