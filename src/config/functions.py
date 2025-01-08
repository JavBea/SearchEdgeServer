#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :functions.py
# @Time      :2025/1/8 15:37
# @Author    :Shao YiHan

# 函数信息
functions = [
    {
        "name": "google_search",
        "description": "Perform a Google search using Custom Search Engine. Highly recommended when you are not available to live data. And get 5 Results!!",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to execute, e.g., 'What is the capital of France?'."
                },
                "num_results": {
                    "type": "integer",
                    "description": "The number of search results to return.",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    }
]


def get_functions():
    """
    返回函数声明
    :return:
    """
    return functions


if __name__ == '__main__':
    code = 0
