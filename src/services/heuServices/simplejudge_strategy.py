#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :simplejudge_strategy.py
# @Time      :2025/1/15 20:01
# @Author    :Shao YiHan
from src.config.llms import LLM


def simple_judge_strategy(llm: str, content: str, query: str):
    """
    简单地判定当前大模型是否陷入幻觉,更侧重于“知识库缺失”引起的幻觉
    :param llm      : 当前回答对应的大模型
    :param content  : 当前的回答
    :param query    : 回答对应的问题
    :return         : (bool) 是否陷入幻觉
    """
    if llm == LLM.CHATGPT.value["series_name"]:
        # 如果当前大模型是ChatGPT
        paer = 1
        # processing code here
    elif llm == LLM.QWEN.value["series_name"]:
        # 如果当前大模型是QWEN
        part = 2
        # processing code here


if __name__ == '__main__':
    codes = 0
