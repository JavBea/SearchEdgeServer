#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :multiquery_strategy.py
# @Time      :2025/1/15 15:10
# @Author    :Shao YiHan

from src.services.llmService import llm_multi_query_service


def multi_query_strategy(query: str, content: str, messages=None, func_on=False):
    """
    根据与向多个大模型同一请求的结果进行比较，来判断指定的大模型是否陷入幻觉
    :param query    : 请求的内容
    :param content  : 指定大模型的返回结果
    :param messages : (dict) 请求的上下文环境；默认为None
    :param func_on  : (bool) 是否开启函数调用；默认为 True,即开启
    :return: 返回
    """
    # 获取多个响应结果
    responses_content = llm_multi_query_service(query=query, messages=messages, func_on=func_on)

    # 添加判定代码。。。。


if __name__ == '__main__':
    aaa = {
        "aaa": "a1",
        "bbb": "b1"
    }
    indexs = 0
    for a in aaa:
        if a == "bbb":
            indexs += 1
    print(indexs)

    codes = 0
