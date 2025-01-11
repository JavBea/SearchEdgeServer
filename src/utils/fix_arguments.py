#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fix_arguments.py
# @Time      :2025/1/11 21:30
# @Author    :Shao YiHan

import json


def fix_arguments(arguments):
    """
    检测并去除 arguments 外部多余的单引号，将其解析为字典。

    :param arguments: 原始的 arguments 数据（可能是字符串或字典）。
    :return: 修复后的字典对象。
    """
    if isinstance(arguments, str):
        # 检查字符串是否被单引号包裹
        if arguments.startswith("'") and arguments.endswith("'"):
            # 去掉外层单引号并尝试解析为 JSON
            arguments = arguments[1:-1].replace("'", '"')  # 将单引号替换为双引号
        try:
            arguments = json.loads(arguments)  # 解析为字典
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format after fixing arguments.")

    if not isinstance(arguments, dict):
        raise TypeError("Expected arguments to be a dictionary.")

    return arguments


if __name__ == "__main__":
    # 测试
    original_arguments = "'{\"query\": \"Python\", \"num_results\": 5}'"
    fixed_arguments = fix_arguments(original_arguments)
    print(fixed_arguments)
