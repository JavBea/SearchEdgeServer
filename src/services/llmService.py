#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llmService.py
# @Time      :2025/1/8 11:06
# @Author    :Shao YiHan

from openai import OpenAI

from src.services.llmServices.gptService import query_service as gpt_query
from src.services.llmServices.qwenService import query_service as qwen_query
from src.services.llmServices.deepseekService import query_service as deepseek_query
from src.config.llms import LLM
from src.config.functions import gpt_functions
from src.config.functions import deepseek_qwen_functions


def llm_query_service(query, llm=LLM.CHATGPT.value["series_name"], model=None, messages=None, func_on=True):
    """

    选择不同系列的大模型、具体模型，在上下文环境和函数说明下，对请求返回结果
    :param query    : (str)  请求的问题
    :param llm      : (str)  请求的大模型系列；默认为 chatgpt
    :param model    : (str)  请求的具体模型； 默认为 None
    :param messages : (dict)  请求的上下文环境；默认为 None
    :param func_on  : (bool) 是否开启函数调用；默认为 True,即开启
    :return : (str) 得到的回答
    """

    # 选择大模型，并调用相关函数
    if llm == LLM.QWEN.value["series_name"]:
        return qwen_query(query, model, messages, deepseek_qwen_functions, func_on)
    elif llm == LLM.DEEPSEEK.value["series_name"]:
        return deepseek_query(query, model, messages, deepseek_qwen_functions, func_on)
    else:
        return gpt_query(query, model, messages, gpt_functions, func_on)


def llm_client_init():
    """
    初始化各个大模型访问客户端实例
    :return: 创建是否成功
    """

    from src.services.llmServices import gptService
    from src.services.llmServices import qwenService
    from src.config import apis
    gptService.client = OpenAI(api_key=apis.GPT_API)
    qwenService.client = OpenAI(
        api_key=apis.QWEN_API,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    return True


def llm_multi_query_service(query, messages=None, func_on=True):
    """
    请求多个模型的结果，用于综合判断大模型是否陷入幻觉
    :param query    : (str)  请求的问题
    :param messages : (dict) 请求的上下文环境；默认为None
    :param func_on  : (bool) 是否开启函数调用；默认为 True,即开启
    :return         : (dict) 返回各个模型的回答
    """
    result = {"chatgpt": gpt_query(query, model=None, messages=messages, functions=gpt_functions, func_on=func_on),
              "qwen": qwen_query(query, model=None, messages=messages, functions=deepseek_qwen_functions, func_on=func_on),
              "deepseek": deepseek_query(query, model=None, messages=messages, functions=deepseek_qwen_functions, func_on=func_on)}
    return result


def llm_single_model_multi_query_service(query, llm, model, messages=None, func_on=True):
    """
    请求多个模型的结果，用于综合判断大模型是否陷入幻觉
    :param query    : (str)  请求的问题
    :param llm      : 指定的大模型
    :param model    : 指定的具体模型
    :param messages : (dict) 请求的上下文环境；默认为None
    :param func_on  : (bool) 是否开启函数调用；默认为 True,即开启
    :return         : (list) 返回各个回答
    """
    # 引入多重查询的次数
    from src.config.constants import SINGLEMODEL_MULTIQUERY_TIMES_ARGUMEMT as TIMES_ARGUMENT
    times = TIMES_ARGUMENT

    result = []

    if llm == LLM.QWEN.value["series_name"]:
        while not times == 0:
            times -= 1
            temp = qwen_query(query, model=model, messages=messages, functions=deepseek_qwen_functions, func_on=func_on)
            result.append(temp)

    elif llm == LLM.DEEPSEEK.value["series_name"]:
        while not times == 0:
            times -= 1
            temp = deepseek_query(query, model=model, messages=messages, functions=deepseek_qwen_functions, func_on=func_on)
            result.append(temp)

    else:
        while not times == 0:
            times -= 1
            temp = gpt_query(query, model=model, messages=messages, functions=gpt_functions, func_on=func_on)
            result.append(temp)

    return result


if __name__ == '__main__':
    llm_client_init()
    # from src.services.heuServices.peerexaminee_strategy import peer_examinee_strategy
    #
    # res2 = peer_examinee_strategy(former_query="Who is Albert Einstein",
    #                               former_content="He is a cat",
    #                               examinee_llm=LLM.QWEN.value['series_name'],
    #                               former_messages=None)
    #
    # print(res2)
    from src.services.heuServices.multiquery_strategy import multi_query_strategy

    res3 = multi_query_strategy(
        query="Who is Albert Einstein",
        content="He is a cat",
    )
    print(res3)

