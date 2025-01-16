#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gptService.py
# @Time      :2025/1/8 10:52
# @Author    :Shao YiHan
import json

from src.services.searchServices.googleService import google_search
from src.models.llm import LLM

client = None


def query_service(query, model=LLM.CHATGPT.value["model1"], messages=None, functions=None, func_on=True):
    """
    向gpt的API问题请求操作，这是向外部文件提供的函数
    :param query    :(str) 请求的问题
    :param model    :(str) 请求建成的模型实例；默认为 "gpt-4o"
    :param messages :(dict) 上下文环境；默认为 None，此时自动生成简单的上下文环境
    :param functions:(dict) 可调用的函数说明；默认为 None
    :param func_on  :(bool) 是否开启函数调用；默认为 True,即开启
    :return : (str) 得到的String格式回复
    """

    # 默认模型为"gpt-4o"
    if model is None:
        model = LLM.CHATGPT.value["model1"]

    # 如果关闭了函数调用
    if (not func_on) or (functions is None):
        # 将函数说明置空，不允许访问进行函数调用，直接返回结果
        response_message = __single_request(query, model, messages, None)
        return response_message.get('content')

    # 如果开启了函数调用，将函数说明传入，并获得初步的答案

    response_message = __single_request(query, model, messages, functions)

    # 循环判断模型是否请求函数调用
    while response_message.get("function_call") is not None:
        function_call = response_message["function_call"]
        function_name = function_call["name"]
        arguments = json.loads(function_call["arguments"])

        # 如果需要调用 google_search
        if function_name == "google_search":
            # 调用Google API进行调用
            result = google_search(query=arguments["query"], num_results=arguments.get("num_results", 3))
            print(result)
            # 将结果返回给大模型
            messages = [
                {"role": "user", "content": query},
                {
                    "role": "assistant",
                    "content": None,
                    "function_call": {
                        "name": function_name,
                        "arguments": json.dumps(arguments)
                    }
                },
                {"role": "function", "name": function_name, "content": result}
            ]

            # 更新响应结果(JSON格式)
            response_message = __single_request(query, model=model, messages=messages, functions=functions)
        # if end
    # while end

    # 得到String类型的文本输出结果
    response_message_content = response_message.get('content')

    # 打印结果
    # print("Final response:", response_message_content)

    # 返回最终结果
    return response_message_content


def __single_request(query, model=LLM.CHATGPT.value["model1"], messages=None, functions=None):
    """
    向gpt的API问题请求操作，这是仅供本文件使用的函数
    :param query    :(str) 请求的问题
    :param model    :(str) 请求建成的模型实例；默认为"gpt-4o"
    :param messages :(dict) 上下文环境；默认为None，此时自动生成简单的上下文环境
    :param functions:(dict) 可调用的函数说明；默认为None
    :return : (dict) 得到的JSON格式回复
    """

    # 生成简单的上下文环境
    if messages is None:
        messages = [{"role": "user", "content": query}]

    # 获取response
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        functions=functions
    )
    # 获取JSON返回数据中的回答字段，并改为dict
    response_message = response.model_dump()["choices"][0]["message"]

    # 返回结果
    return response_message


if __name__ == '__main__':
    # res = __single_request("What is pycharm")
    # print(res)
    # print(res.get('content'))

    res2 = query_service("Who won the 2024 US presidential election")
    print(res2)

    from src.config.functions import gpt_functions as declarations

    res2 = query_service("Who won the 2024 US presidential election", model="gpt-4o", messages=None,
                         functions=declarations, func_on=True)
    print("RAG response: " + res2)
