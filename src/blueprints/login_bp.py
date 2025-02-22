#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_bp.py
# @Time      :2025/1/13 18:48
# @Author    :Shao YiHan
from flasgger import swag_from
from flask import request
import flask

from src.dao.UserDao import UserDao
from src.utils.json_generator.login_response_json import LoginResponseJson

# 实例化蓝图对象“login_bp”
login_bp = flask.Blueprint('login_module', __name__)


@login_bp.route('/login', methods=['POST'])
@swag_from('../../static/swagger/login.yaml')
def login():
    """
    登录验证请求
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
