#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conversation_bp.py
# @Time      :2025/1/14 9:39
# @Author    :Shao YiHan

from flask import request
import flask

from src.dao.ConversationDao import ConversationDao
from src.utils.json_generator.conversation_response_json import ConversationResponseJson

# 实例化蓝图对象“conversation_bp”
conversation_bp = flask.Blueprint('conversation_module', __name__)


@conversation_bp.route('/getallconversations', methods=['POST'])
def get_all_conversations():

    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    user_id = data['user_id']

    conversations = ConversationDao.get_all_conversations_by_user_id(user_id)

    res = ConversationResponseJson.conversations_to_json(conversations)

    print(res)

    return res


if __name__ == '__main__':
    codes = 0
