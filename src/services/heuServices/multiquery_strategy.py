#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :multiquery_strategy.py
# @Time      :2025/1/15 15:10
# @Author    :Shao YiHan
from langdetect import detect

from src.config.heus import MultiQueryStrategy
from src.config.heus import SemanticMatchingStrategy
from src.services.llmService import llm_multi_query_service, llm_single_model_multi_query_service, llm_client_init


def multi_query_strategy(query: str, content: str, messages=None, func_on=False,
                         query_method=MultiQueryStrategy.METHOD1.value,
                         matching_method=SemanticMatchingStrategy.METHOD2.value, llm=None, model=None):
    """
    **多反馈策略**
    根据与向多个同一请求的反馈结果进行比较，来判断指定的大模型是否陷入幻觉
    :param query            : 请求的内容
    :param content          : 指定大模型的返回结果
    :param messages         : (dict) 请求的上下文环境；默认为None
    :param func_on          : (bool) 是否开启函数调用；默认为 True,即开启
    :param query_method     : (int) 采用的多次请求方案
    :param matching_method  : (int) 采用的语义匹配方案
    :param llm              : 指定的大模型
    :param model            : 指定的具体模型
    :return: 返回一个百分比数字，代表模型未陷入幻觉的可能性
    """

    # 引入语义匹配方案
    if matching_method == SemanticMatchingStrategy.METHOD1.value:
        if detect(query) == 'zh':
            from src.utils.heu_kits.tfidf_methods import tfidf_similarity_chinese as compute_similarity
        else:
            from src.utils.heu_kits.tfidf_methods import tfidf_similarity_english as compute_similarity
    else:
        from src.utils.heu_kits.bert_methods import bert_similarity as compute_similarity

    # 存储响应结果
    res_list = []

    # 获取多个响应结果
    if query_method == MultiQueryStrategy.METHOD1.value:
        res_list = llm_single_model_multi_query_service(query=query, messages=messages, func_on=func_on, llm=llm,
                                                        model=model)
    elif query_method == MultiQueryStrategy.METHOD2.value:
        res_list = llm_multi_query_service(query=query, messages=messages, func_on=func_on)

    print(res_list)

    # 相似度之和
    similarity_sum = 0

    # 遍历响应结果集合
    index = len(res_list)
    while index > 0:
        index -= 1
        # 计算相似度评分和
        similarity_sum += compute_similarity(res_list[index], content)
        print(similarity_sum)

    # 计算平均值
    similarity_average = similarity_sum / len(res_list)

    # 按不同方案的预设参数调整结果
    if matching_method == SemanticMatchingStrategy.METHOD1.value:
        from src.config.constants import TFIDF_ARGUMEMT
        similarity_average *= TFIDF_ARGUMEMT
    else:
        from src.config.constants import BERT_ARGUMEMT
        similarity_average *= BERT_ARGUMEMT

    # 防止分数溢出
    if similarity_average > 100:
        similarity_average = 100

    return similarity_average


if __name__ == '__main__':
    llm_client_init()
    contents = "I am an AI designed to assist and provide information on a wide range of topics. I can answer questions, help with problem-solving, provide explanations, and offer recommendations based on the information I have been trained on. If you have any questions or need assistance, feel free to ask!"
    result = multi_query_strategy(query="Who are you?", content=contents, llm="chatgpt", model="gpt-4o", messages=None, func_on=True,)

    print(result)

    codes = 0
