#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :message_bp.py
# @Time      :2025/1/14 16:16
# @Author    :Shao YiHan
from flask import request
import flask

from src.services.modelServices.MessageService import MessageService
from src.utils.json_generator.message_response_json import MessageResponseJson

# 实例化蓝图对象“message_bp”
message_bp = flask.Blueprint('message_module', __name__)


@message_bp.route('/getallmessages', methods=['POST'])
def get_all_messges():
    # 获取请求
    data = request.get_json()

    # 获取请求的各个字段
    conversation_id = data['conversation_id']

    messages = MessageService.get_messages_by_conversation_id(conversation_id)

    res = MessageResponseJson.messages_to_json(messages)

    return res


@message_bp.route('/createmessage', methods=['POST'])
def create_all_messges():
    # 获取请求
    data = request.get_json()

    # 获取请求的各个字段
    conversation_id = data['conversation_id']
    sender = data['sender']
    content = data['content']

    message = MessageService.create_message(conversation_id=conversation_id, sender=sender, message_content=content)

    res = MessageResponseJson(message=message)

    return res.to_json()


if __name__ == '__main__':
    codes = 0
