#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :message_response_json.py
# @Time      :2025/1/14 16:52
# @Author    :Shao YiHan
import json
from typing import List

from src.models.message import Message


class MessageResponseJson:
    """
    生成请求消息回复时的JSON格式类
    """

    def __init__(self, message: Message):
        """
        类初始化函数
        :param message  : 当前会话
        """
        self.message = message

    def to_dict(self):
        """
        返回字典格式的数据
        :return: 返回符合设计的 JSON 结构
        """

        if self.message is None:
            response = {
                "code": "404"
            }
            return response

        response = {
            "id": self.message.id,
            "conversation_id": self.message.conversation_id,
            "sender": self.message.sender,
            "message_content": self.message.message_content,
            "created_at": self.message.created_at.isoformat() if self.message.created_at else None,
        }
        return response

    def to_json(self):
        """
        返回JSON格式的数据
        :return: 将字典转换为 JSON 格式的字符串
        """
        return json.dumps(self.to_dict(), indent=4)

    @staticmethod
    # 将 list[message] 转化为 JSON
    def messages_to_json(messages: List[Message]) -> str:
        if messages is None:
            response = {
                "code": "404"
            }
            return json.dumps(response)

        # 使用 list comprehension 调用每个对象的 to_dict 方法
        messages_dict = [MessageResponseJson(message).to_dict() for message in messages]
        # 将列表字典序列化为 JSON 字符串
        return json.dumps(messages_dict, indent=4)


if __name__ == '__main__':
    codes = 0
