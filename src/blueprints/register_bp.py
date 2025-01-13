#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :register_bp.py
# @Time      :2025/1/13 22:48
# @Author    :Shao YiHan
from flask import request
import flask

from src.services.UserService import UserService
from src.utils.json_generator.register_response_json import RegisterResponseJson

# 实例化蓝图对象“llm”
register_bp = flask.Blueprint('register_module', __name__)


@register_bp.route('/register', methods=['POST'])
def register():
    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    user_name = data['user_name']
    password = data['password']
    email = data['email']

    user, code = UserService.create_user(password=password, email=email, user_name=user_name)

    res = RegisterResponseJson(user, code)

    return res.to_json()


if __name__ == '__main__':
    codes = 0
