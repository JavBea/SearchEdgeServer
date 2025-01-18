#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llms.py
# @Time      :2025/1/15 16:11
# @Author    :Shao YiHan
from enum import Enum


class LLM(Enum):
    """
    为了统一字符串，设置大模型的枚举类型
    每个键是一个大模型系列，每个键中的第一个为该大模型系列名，后续为可选的具体模型名
    """
    CHATGPT = {
        "series_name": "chatgpt",
        "model1": "gpt-4o",
        "model2": "gpt-4mini"
    }
    QWEN = {
        "series_name": "qwen",
        "model1": "qwen-plus",
        "model2": "qwen-4"
    }


if __name__ == '__main__':
    print(LLM.CHATGPT.value["series_name"])
