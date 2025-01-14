#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conversation_response_json.py
# @Time      :2025/1/14 11:38
# @Author    :Shao YiHan

import json
from typing import List

from src.models.conversation import Conversation


class ConversationResponseJson:
    """
    生成会话请求回复时的JSON格式类
    """

    def __init__(self, conversation: Conversation):
        """
        类初始化函数
        :param conversation  : 当前会话
        """
        self.conversation = conversation

    def to_dict(self):
        """
        返回字典格式的数据
        :return: 返回符合设计的 JSON 结构
        """

        if self.conversation is None:
            response = {
                "code": "404"
            }
            return response

        response = {
            "id": self.conversation.id,
            "user_id": self.conversation.user_id,
            "title": self.conversation.title,
            "created_at": self.conversation.created_at.isoformat() if self.conversation.created_at else None,
            "updated_at": self.conversation.updated_at.isoformat() if self.conversation.updated_at else None,
        }
        return response

    def to_json(self):
        """
        返回JSON格式的数据
        :return: 将字典转换为 JSON 格式的字符串
        """
        return json.dumps(self.to_dict(), indent=4)

    @staticmethod
    # 将 list[Conversation] 转化为 JSON
    def conversations_to_json(conversations: List[Conversation]) -> str:
        if conversations is None:
            response = {
                "code": "404"
            }
            return json.dumps(response)

        # 使用 list comprehension 调用每个对象的 to_dict 方法
        conversations_dict = [ConversationResponseJson(conversation).to_dict() for conversation in conversations]
        # 将列表字典序列化为 JSON 字符串
        return json.dumps(conversations_dict, indent=4)


if __name__ == '__main__':
    codes = 0
