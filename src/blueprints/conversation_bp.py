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
    """
    获取全部会话请求
    ---
    tags:
      - Conversation API
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 获取全部会话请求
          required:
            - user_id
          properties:
            user_id:
              type: string
              description: 用户ID.
              example: 10000002

    responses:
      200:
        description: Successful processing of the request
        schema:
          id: 获取全部会话请求响应
          properties:
            id:
              type: int
              description: 会话ID
            user_id:
              type: int
              description: 用户ID
            title:
              type: string
              description: 会话标题
            created_at:
              type: string
              description: 会话创建时间
            updated_at:
              type: string
              description: 会话最后更新时间
        examples:
          application/json: [{"id": 10001,"user_id": 10000002,"title": "\u5bf9\u8bdd2.1",
          "created_at": "2025-01-13T15:55:13","updated_at": "2025-01-13T15:57:38"},...]
    """
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
