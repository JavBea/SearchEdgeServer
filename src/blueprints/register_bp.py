#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :register_bp.py
# @Time      :2025/1/13 22:48
# @Author    :Shao YiHan
from flask import request
import flask

from src.dao.UserDao import UserDao
from src.utils.json_generator.register_response_json import RegisterResponseJson

# 实例化蓝图对象“register_bp”
register_bp = flask.Blueprint('register_module', __name__)


@register_bp.route('/register', methods=['POST'])
def register():
    """
    注册请求
    ---
    tags:
      - Register API
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 注册请求
          required:
            - user_name
            - password
            - email
          properties:
            user_name:
              type: string
              description: 用户名.
              example: "userrr"
            password:
              type: string
              description: 密码
              example: "1223666a"
            email:
              type: string
              description: 绑定的邮箱.
              example: "ggttg@me.you"
    responses:
      200:
        description: Successful processing of the request
        schema:
          id: 注册请求响应
          properties:
            code:
              type: string
              description: 请求响应码
            status:
              type: boolean
              description: 账号可用性
            user_id:
              type: int
              description: 用户ID
            user_name:
              type: string
              description: 用户名
            email:
              type: string
              description: 绑定的邮箱
            role:
              type: string
              description: 用户身份
        examples:
          application/json: {"code": "2001","status": "available","user_id": 10000002,"user_name": "user",
          "email": "user@gmail.com","role": "user"}
    """
    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    user_name = data['user_name']
    password = data['password']
    email = data['email']

    user, code = UserDao.create_user(password=password, email=email, user_name=user_name)

    res = RegisterResponseJson(user, code)

    return res.to_json()


if __name__ == '__main__':
    codes = 0
