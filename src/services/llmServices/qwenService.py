#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :qwenService.py
# @Time      :2025/1/8 11:34
# @Author    :Shao YiHan

def query_service(query, model="qwen-plus", messages=None, functions=None):
    """
    通过千问大模型的api来获取对应问题的答案
    :param query    :(str) 请求的问题
    :param model    :(str) 请求建成的模型实例；默认为"qwen-plus"
    :param messages :(dict) 上下文环境；默认为None，此时自动生成简单的上下文环境
    :param functions:(dict) 可调用的函数说明；默认为None
    :return : (str) 得到的回答

    """
    return "Corrent module is under maintence!"


if __name__ == '__main__':
    code = 0
