#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :register_response_json.py
# @Time      :2025/1/13 22:54
# @Author    :Shao YiHan
import json

from src.models.user import User


class RegisterResponseJson:
    """
    生成注册请求回复时的JSON格式类
    """

    def __init__(self, user: User, code: str):
        """
        类初始化函数
        :param user  : 当前登录的模型
        :param code  : 注册返回码
        """
        self.user = user
        self.code = code

    def to_dict(self):
        """
        返回字典格式的数据
        :return: 返回符合设计的 JSON 结构
        """

        if self.user is None:
            response = {
                "code": self.code
            }
            return response

        response = {
            "code": self.code,
            "status": self.user.status,
            "user_id": self.user.user_id,
            "user_name": self.user.user_name,
            "email": self.user.email,
            "role": self.user.role
        }
        return response

    def to_json(self):
        """
        返回JSON格式的数据
        :return: 将字典转换为 JSON 格式的字符串
        """
        return json.dumps(self.to_dict(), indent=4)


if __name__ == '__main__':
    codes = 0
