#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_bp.py
# @Time      :2025/1/13 18:48
# @Author    :Shao YiHan

from flask import request
import flask

from src.dao.UserDao import UserDao
from src.utils.json_generator.login_response_json import LoginResponseJson

# 实例化蓝图对象“login_bp”
login_bp = flask.Blueprint('login_module', __name__)


@login_bp.route('/login', methods=['POST'])
def login():
    """
    登录验证请求
    ---
    tags:
      - Login API
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 登录验证请求
          required:
            - token
            - password
          properties:
            token:
              type: string
              description: 登录的用户名或邮箱.
              example: "user"
            password:
              type: string
              description: 登录密码
              example: "123456a"

    responses:
      200:
        description: Successful processing of the request
        schema:
          id: 登录验证请求响应
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
    token = data['token']
    password = data['password']

    user, code = UserDao.check_user(token, password)

    res = LoginResponseJson(user,code)

    return res.to_json()


if __name__ == '__main__':
    codes = 0
