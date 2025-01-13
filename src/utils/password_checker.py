#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :password_checker.py
# @Time      :2025/1/13 23:17
# @Author    :Shao YiHan
import re

def is_valid_password(password):
    """
    检查密码格式是否正确。
    要求：
    - 至少 6 个字符
    - 至少包含数字和字母
    :param password: str
    :return: bool
    """
    if len(password) < 6:
        return False

    # 使用正则表达式检查是否包含字母和数字
    has_letter = bool(re.search(r'[a-zA-Z]', password))
    has_digit = bool(re.search(r'\d', password))

    return has_letter and has_digit


if __name__ == '__main__':
    # 测试
    passwords = [
        "123456",  # 只有数字
        "abcdef",  # 只有字母
        "abc123",  # 有字母和数字，长度合格
        "a1",  # 有字母和数字，但长度不足
        "password123",  # 符合要求
    ]

    for pwd in passwords:
        print(f"密码: {pwd}, 格式正确: {is_valid_password(pwd)}")
