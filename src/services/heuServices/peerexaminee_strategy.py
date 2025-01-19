#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :peerexaminee_strategy.py
# @Time      :2025/1/15 21:51
# @Author    :Shao YiHan
from src.config.llms import LLM
from src.services.llmService import llm_query_service
from src.utils.heu_kits.peerexaminee_methods import extract_bool


# 同伴策略
def peer_examinee_strategy(former_query: str, former_content: str, examinee_llm: int, former_messages=None):
    """
    同伴策略来判断大模型是否陷入幻觉。
    同伴策略用到两个大模型，一个作为examinee，即待测者，另一个作为examiner，即检验者。
    :param former_query     : (str)之前请求的内容
    :param former_content   : (str)之前的回复
    :param examinee_llm     : (int)待测的大模型
    :param former_messages  : (list)之前的上下文环境
    :return                 : (int)可信度
    """
    # 生成请求模板
    query_head = ("I want you to determine whether the answers of a large model fall into an illusion. Here's the "
                  "information. The messages field represents the context, the query field represents the content of "
                  "the request, and the Content field represents the response of the large model:")
    query_body = "messages:\n"+str(former_messages)+"\n"+"query:"+former_query+"\n"+"content:\n"+former_content
    query_foot = ("Return the value in the format of result=(bool), where False indicates that you are not "
                  "hallucinating and True indicates that you are hallucinating")

    # 组成完整请求
    query = query_head+query_body+query_foot

    # 选取合适的examiner LLM
    if examinee_llm == LLM.CHATGPT.value:
        # 如果examinee为ChatGPT就选QWEN作examiner
        result = llm_query_service(query=query, llm=LLM.QWEN.value, messages=former_messages, func_on=False)
    else:
        # 默认选ChatGPT作examiner
        result = llm_query_service(query=query, llm=LLM.CHATGPT.value, messages=former_messages, func_on=False)

    # print(result)

    # 从评测结果中提取结果，如果认为陷入幻觉则返回0，否则返回100
    if extract_bool(result):
        return 0
    else:
        return 100


if __name__ == '__main__':
    codes = 0
