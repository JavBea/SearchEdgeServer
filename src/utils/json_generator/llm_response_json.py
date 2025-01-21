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

    def __init__(self, content, heu_result, status=False):
        """
        类初始化函数
        :param content      : (str) 主要内容，成功时为大模型的回复，失败时为错误信息
        :param heu_result   : (dict) 启发式规则请求结果
        :param status       : (bool) 是否成功
        """
        self.heu_result = heu_result
        self.content = content
        self.status = status

    def to_dict(self):
        """
        返回字典格式的数据
        :return: 返回符合设计的 JSON 结构
        """
        response = {
            "status": self.status,
            "content": self.content,
            "heu_result": self.heu_result
        }
        return response

    def to_json(self):
        """
        返回JSON格式的数据
        :return: 将字典转换为 JSON 格式的字符串
        """
        return json.dumps(self.to_dict(), indent=4)

    @staticmethod
    def multi_to_json(responses: dict):
        """
        含有多个大模型响应结果的字典转化为JSON格式
        :param responses: 含有多个响应结果的字典
        :return         : json格式的responses
        """
        if responses is None:
            response = {
                "code": "404"
            }
            return json.dumps(response)

        # 将列表字典序列化为 JSON 字符串
        return json.dumps(responses, indent=4)


if __name__ == '__main__':
    code = 0
