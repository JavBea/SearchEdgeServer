#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :heus.py
# @Time      :2025/1/18 10:38
# @Author    :Shao YiHan
from enum import Enum, auto


# 启发式规则各种策略
class HeuStrategy(Enum):
    # 简约策略
    SIMPLEJUDGE = auto()
    # 多反馈策略
    MULTIQUERY = auto()
    # 函数调用策略
    FUNCTIONCALL = auto()
    # 多模型交互策略
    PEEREXAMINEE = auto()


# 多反馈策略的预设方案
class MultiQueryStrategy(Enum):
    # 向同一模型多次请求的策略,默认三次
    METHOD1 = auto()
    # 向多个模型单次请求的策略,默认三个模型各一次
    METHOD2 = auto()


# 语义匹配的预设方案
class SemanticMatchingStrategy(Enum):
    # tf-idf方案，精度很低
    METHOD1 = auto()
    # BERT方案，精度较高
    METHOD2 = auto()


if __name__ == '__main__':
    codes = 0
