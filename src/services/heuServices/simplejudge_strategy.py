#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :simplejudge_strategy.py
# @Time      :2025/1/15 20:01
# @Author    :Shao YiHan
from src.config.llms import LLM
from src.config.searchs import SearchStrategy

from src.utils.heu_kits.simple_methods import extract_and_validate_equations
from src.utils.heu_kits.simple_methods import validate_year_and_month
from src.utils.heu_kits.simple_methods import search_pattern

from src.services.searchService import search_service


def simple_judge_strategy(llm: str, content: str, query: str):
    """
    通过一些简约的方法，针对特定问题（大模型经常出现幻觉的问题），判定当前大模型是否陷入幻觉
    :param llm      : 当前回答对应的大模型
    :param content  : 当前的回答内容
    :param query    : 回答对应的问题
    :return         : (float) 未陷入幻觉 (大模型可靠)的概率
    """

    # 数学等式的检查
    valid_equations, invalid_equations = extract_and_validate_equations(content)
    # 取正确等式的比例作为第一个参数
    args1 = len(valid_equations)/(len(valid_equations)+len(invalid_equations))

    # 简单信息检查(时间匹配)
    # 获得str类型的搜索结果
    search_result = search_service(query=query, method=SearchStrategy.GOOGLESEARCH.value, num_results=5)
    args2 = validate_year_and_month(refernce=search_result, candidate=content)

    # 知识库缺失检查（特征文本检测）
    # 根据历史经验来判断大模型是否陷入幻觉
    args3 = 100
    if llm == LLM.CHATGPT.value["series_name"]:
        # 如果当前大模型是ChatGPT
        args3 -= 30 if search_pattern(content,"I'm sorry") else 0
        args3 -= 50 if search_pattern(content,"after October 2023") else 0
        args3 -= 30 if search_pattern(content,"抱歉") else 0
        args3 -= 50 if search_pattern(content,"知识更新截止") else 0

    elif llm == LLM.QWEN.value["series_name"]:
        # 如果当前大模型是QWEN
        # 匹配到一次特征文本即减一定分数
        args3 -= 50 if search_pattern(content,"last update") else 0
        args3 -= 30 if search_pattern(content,"无法预测") else 0

    # 返回平均分
    return (args1+args2+args3)/3


if __name__ == '__main__':
    codes = 0
