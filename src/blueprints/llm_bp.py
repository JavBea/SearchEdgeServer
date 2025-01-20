#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llm_bp.py
# @Time      :2025/1/8 10:28
# @Author    :Shao YiHan
from flask import request
import flask

from src.services import llmService
from src.utils.json_generator.llm_response_json import LlmResponseJson

# 实例化蓝图对象“llm_bp”
llm_bp = flask.Blueprint('llm_module', __name__)


@llm_bp.route('/query', methods=['POST'])
def query_route():
    """
    This endpoint processes a POST request with a JSON body containing
    'query' and 'func_on' fields and returns a JSON response with 'content'
    and 'status' fields.
    ---
    tags:
      - Example API
    parameters:
      - name: query
        in: body
        required: true
        type: string
        description: The query string for processing.
        example: "select * from users"
      - name: func_on
        in: body
        required: true
        type: string
        description: The function or action to perform on the query.
        example: "execute"
    responses:
      200:
        description: Successful processing of the request
        content:
          application/json:
            schema:
              type: object
              properties:
                content:
                  type: string
                  description: The result of the query execution or action.
                  example: "Query executed successfully."
                status:
                  type: string
                  description: The status of the request.
                  example: "success"
      400:
        description: Invalid input data
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: The error message explaining why the request failed.
                  example: "Missing required fields."
    :return:
    """
    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    query = data['query']
    func_on = data['func_on']
    llm = data['llm']
    model = data['model']

    # 获得请求内容
    response_message_content = llmService.llm_query_service(query, llm=llm, model=model, func_on=func_on)
    res = LlmResponseJson(response_message_content, True)
    return res.to_json()


@llm_bp.route('/multiquery', methods=['POST'])
def multi_query_route():
    """
    ---
    $ref: './swagger/test.yaml'
    :return:
    """
    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    query = data['query']
    func_on = data['func_on']

    # 获得请求内容
    responses_content = llmService.llm_multi_query_service(query, func_on=func_on)
    res = LlmResponseJson.multi_to_json(responses_content)
    return res


if __name__ == '__main__':
    response = LlmResponseJson("AAA-猪肉批发", True)
    print(response.to_json())
