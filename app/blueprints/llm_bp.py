#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llm_bp.py
# @Time      :2025/1/8 10:28
# @Author    :Shao YiHan
from flask import request
import flask

from app.services import llmService
from app.utils.json_generator.llm_response_json import LlmResponseJson

# 实例化蓝图对象“llm”
llm_bp = flask.Blueprint('llm_module', __name__)


@llm_bp.route('/query', methods=['POST'])
def query_route():
    # 获取请求的各个字段
    data = request.get_json()
    query = data['query']
    func_on = data['func_on']
    llm = data['llm']
    model = data['model']

    # 获得请求内容
    response_message_content = llmService.llm_query_service(query, llm=llm, model=model, func_on=func_on)
    res = LlmResponseJson(response_message_content, True)
    return res.to_json()


if __name__ == '__main__':
    response = LlmResponseJson("AAA-猪肉批发", True)
    print(response.to_json())
