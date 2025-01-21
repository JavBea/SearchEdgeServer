#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :heuService.py
# @Time      :2025/1/13 17:03
# @Author    :Shao YiHan

def illusion_judge(heu_list: dict, content: str, query: str, llm, model, func_on=True, messages=None):
    """
    幻觉判定方法
    :param heu_list : (dict) 选取的启发式规则策略
    :param content  : (str) 待测的大模型响应内容
    :param query    : (str) 原本的请求内容
    :param llm      : (str) 原本请求的大模型
    :param model    : (str) 原本请求的具体模型
    :param func_on  : (bool) 是否开启函数调用
    :param messages : (list) 原本的上下文信息
    :return         : (dict) 选取的各模型评估结果，未选取的置 None
    """

    result = {
        'SIMPLEJUDGE': None,
        'MULTIQUERY': None,
        'FUNCTIONCALL': None,
        'PEEREXAMINEE': None
    }

    if heu_list is None:
        return result

    # 各个策略是否选取
    sj = heu_list.get('SIMPLEJUDGE')
    mp = heu_list.get('MULTIQUERY')
    fc = heu_list.get('FUNCTIONCALL')
    pe = heu_list.get('PEEREXAMINEE')

    if sj:
        from src.services.heuServices.simplejudge_strategy import simple_judge_strategy
        result['SIMPLEJUDGE'] = simple_judge_strategy(llm=llm, query=query, content=content)

    if mp:
        from src.services.heuServices.multiquery_strategy import multi_query_strategy
        result['MULTIQUERY'] = multi_query_strategy(query=query, content=content, llm=llm, model=model, func_on=func_on)

    if fc:
        from src.services.heuServices.functioncall_strategy import function_call_strategy
        result['FUNCTIONCALL'] = function_call_strategy(content=content, query=query)

    if pe:
        from src.services.heuServices.peerexaminee_strategy import peer_examinee_strategy
        result['PEEREXAMINEE'] = peer_examinee_strategy(former_query=query, former_content=content,
                                                        examinee_llm=llm, former_messages=messages)

    return result


def illusion_remit():
    """
    幻觉缓解方法
    :return:
    """
    return True


if __name__ == '__main__':
    code = 0
