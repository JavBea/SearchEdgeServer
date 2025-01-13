#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :email_checker.py
# @Time      :2025/1/13 23:55
# @Author    :Shao YiHan
import re


def is_valid_email(email):
    """
    检查字符串是否为有效的邮箱地址。
    要求：
    - 包含 "@" 符号
    - "@" 前后都有内容
    - 域名部分包含 "."，且不以 "." 开头或结尾

    :param email: str
    :return: bool
    """
    # 使用正则表达式验证邮箱格式
    pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    return bool(re.match(pattern, email))


if __name__ == '__main__':
    emails = [
        "test@example.com",  # 合法邮箱
        "invalid-email",  # 缺少 @ 和域名
        "user@.com",  # 域名以 . 开头
        "@example.com",  # 缺少用户名
        "user@example",  # 缺少顶级域名
        "user@sub.example.com"  # 合法邮箱
    ]

    for email in emails:
        print(f"邮箱: {email}, 格式正确: {is_valid_email(email)}")
