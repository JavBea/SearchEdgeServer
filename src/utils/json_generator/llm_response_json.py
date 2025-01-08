#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llm_response_json.py
# @Time      :2025/1/8 17:18
# @Author    :Shao YiHan
import json


class LlmResponseJson:
    """
    生成大模型进行回复时的JSON格式类
    """
    def __init__(self, content, status=False):
        """
        类初始化函数
        :param content : (str) 主要内容，成功时为大模型的回复，失败时为错误信息
        :param status  : (bool) 是否成功
        """
        self.content = content
        self.status = status

    def to_dict(self):
        """
        返回字典格式的数据
        :return: 返回符合设计的 JSON 结构
        """
        response = {
            "status": self.status,
            "content": self.content
        }
        return response

    def to_json(self):
        """
        返回JSON格式的数据
        :return: 将字典转换为 JSON 格式的字符串
        """
        return json.dumps(self.to_dict(), indent=4)


if __name__ == '__main__':
    code = 0
