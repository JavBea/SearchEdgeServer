#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :peerexaminee_methods.py
# @Time      :2025/1/19 19:08
# @Author    :Shao YiHan

import re


# 从examiner LLM的回答中找到目标部分
def extract_bool(text):
    # 正则表达式，匹配 result= 后跟可能有空格的 True/False
    match = re.search(r'result\s*=\s*(True|False)', text, re.IGNORECASE)
    if match:
        return match.group(1).strip().lower() == 'true'
    return None


if __name__ == '__main__':
    text = "some text result =  false  more text"
    bool_value = extract_bool(text)
    print(bool_value)
