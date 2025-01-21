#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :message_bp.py
# @Time      :2025/1/14 16:16
# @Author    :Shao YiHan
from flask import request
import flask

from src.dao.MessageDao import MessageDao
from src.utils.json_generator.message_response_json import MessageResponseJson

# 实例化蓝图对象“message_bp”
message_bp = flask.Blueprint('message_module', __name__)


@message_bp.route('/getallmessages', methods=['POST'])
def get_all_messges():
    """
    获取会话全部信息请求
    ---
    tags:
      - Message API
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 获取会话全部信息请求
          required:
            - conversation_id
          properties:
            conversation_id:
              type: int
              description: 会话ID.
              example: 10001

    responses:
      200:
        description: Successful processing of the request
        schema:
          id: 获取会话全部信息请求响应
          properties:
            id:
              type: int
              description: 消息ID
            conversation_id:
              type: int
              description: 会话ID
            sender:
              type: string
              description: 发送方
            message_content:
              type: string
              description: 消息内容
            created_at:
              type: string
              description: 消息创建时间
        examples:
          application/json: [{"id": 10000001,"conversation_id": 10001,"sender": "user",
          "message_content": "aaa","created_at": "2025-01-13T16:03:37"},...]
    """
    # 获取请求
    data = request.get_json()

    # 获取请求的各个字段
    conversation_id = data['conversation_id']

    messages = MessageDao.get_messages_by_conversation_id(conversation_id)

    res = MessageResponseJson.messages_to_json(messages)

    return res


@message_bp.route('/createmessage', methods=['POST'])
def create_message():
    # 获取请求
    data = request.get_json()

    # 获取请求的各个字段
    conversation_id = data['conversation_id']
    sender = data['sender']
    content = data['content']

    message = MessageDao.create_message(conversation_id=conversation_id, sender=sender, message_content=content)

    res = MessageResponseJson(message=message)

    return res.to_json()


if __name__ == '__main__':
    codes = 0
