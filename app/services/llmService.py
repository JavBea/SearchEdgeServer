#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llmService.py
# @Time      :2025/1/8 11:06
# @Author    :Shao YiHan
import json


def llm_query_service(query, llm="chatgpt", model=None, messages=None, functions=None, func_on=True):
    """
    选择不同系列的大模型、具体模型，在上下文环境和函数说明下，对请求返回结果
    :param query    : (str)  请求的问题
    :param llm      : (str)  请求的大模型系列；默认为chatgpt
    :param model    : (str)  请求的具体模型； 默认为None
    :param messages : (dict)  请求的上下文环境；默认为None
    :param functions: (dict)  可供调用的函数说明；默认为None
    :param func_on  : (bool) 是否开启函数调用；默认为 True,即开启
    :return : (str) 得到的回答
    """

    # 选择大模型，并引入相关函数
    if llm == "chatgpt":
        from llmServices.gptService import query_service
    else:
        from llmServices.qwenService import query_service

    # 返回结果
    return query_service(query, model, messages, functions, func_on)


if __name__ == '__main__':
    from app.config.functions import functions as declarations

    res2 = llm_query_service("Who won the 2024 US presidential election", model="gpt-4o", messages=None,
                             functions=declarations, func_on=True)
    print("RAG response: " + res2)
