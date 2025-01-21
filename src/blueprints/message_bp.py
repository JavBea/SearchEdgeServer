#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :message_bp.py
# @Time      :2025/1/14 16:16
# @Author    :Shao YiHan
from flasgger import swag_from
from flask import request
import flask

from src.dao.MessageDao import MessageDao
from src.utils.json_generator.message_response_json import MessageResponseJson

# 实例化蓝图对象“message_bp”
message_bp = flask.Blueprint('message_module', __name__)


@message_bp.route('/getallmessages', methods=['POST'])
@swag_from('../../static/swagger/getallmessages.yaml')
def get_all_messges():
    """
    获取会话全部信息请求
    """
    # 获取请求
    data = request.get_json()

    # 获取请求的各个字段
    conversation_id = data['conversation_id']

    messages = MessageDao.get_messages_by_conversation_id(conversation_id)

    res = MessageResponseJson.messages_to_json(messages)

    return res


@message_bp.route('/createmessage', methods=['POST'])
@swag_from('../../static/swagger/createmessage.yaml')
def create_message():
    """
    创建消息
    """
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
