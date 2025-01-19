#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :functioncall_methods.py
# @Time      :2025/1/15 19:24
# @Author    :Shao YiHan
from src.config.searchs import SearchStrategy
from src.services.searchService import search_service
from src.utils.heu_kits.functioncall_methods import calculate_reliability


# 函数调用策略
def function_call_strategy(content: str, query: str):
    """
    将函数调用结果作为参考文本与结果进行比较，主要是文本中的 "实体" 对比, 提取两个文本中出现的实体，包括人名、物名、时间等来判断两个文本的相似度
    :param content  : (str) 当前的回答内容
    :param query    : (str) 请求的内容
    :return         : (int) 可信度分数
    """
    # 请求结果
    search_result = search_service(query=query, method=SearchStrategy.GOOGLESEARCH.value, num_results=5)
    # 计算分数
    score = calculate_reliability(reference=search_result, candidate=content)

    return score


if __name__ == '__main__':
    codes = 0
