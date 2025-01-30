#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :llm_bp.py
# @Time      :2025/1/8 10:28
# @Author    :Shao YiHan
from flasgger import swag_from
from flask import request
import flask

from src.services import llmService
from src.services import heuService
from src.utils.json_generator.llm_response_json import LlmResponseJson
from src.dao.MessageDao import MessageDao

# 实例化蓝图对象“llm_bp”
llm_bp = flask.Blueprint('llm_module', __name__)


@llm_bp.route('/query', methods=['POST'])
@swag_from('../../static/swagger/llm_query.yaml')
def query_route():
    """
    向大模型的单次请求
    """
    # 获取请求
    data = request.get_json()
    # 获取请求的各个字段
    query = data['query']
    func_on = data['func_on']
    heu_on = data['heu_on']
    llm = data['llm']
    model = data['model']
    conversation_id = data['conversation_id']

    # 将用户发送的请求写入数据库
    MessageDao.create_message(
        conversation_id=conversation_id,
        sender='user',
        message_content=query,
    )

    # 获得请求内容
    response_message_content = llmService.llm_query_service(query, llm=llm, model=model, func_on=func_on)

    # 将大模型响应结果写入数据库
    MessageDao.create_message(
        conversation_id=conversation_id,
        sender='system',
        message_content=response_message_content,
    )

    # 如果打开启发式规则就获取请求的启发式规则策略列表，否则置None
    heu_list = data.get('heu_list', None) if heu_on else None

    # 获取评分结果
    heu_result = heuService.illusion_judge(
        heu_list=heu_list,
        content=response_message_content,
        query=query,
        llm=llm,
        model=model,
    )

    # 生成响应实例
    res = LlmResponseJson(content=response_message_content, heu_result=heu_result,status=True)

    return res.to_json()


@llm_bp.route('/multiquery', methods=['POST'])
@swag_from('../../static/swagger/llm_multiquery.yaml')
def multi_query_route():
    """
    向大模型的多重请求
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
