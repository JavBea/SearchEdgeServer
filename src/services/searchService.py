#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :searchService.py
# @Time      :2025/1/12 16:02
# @Author    :Shao YiHan

from src.services.searchServices.googleService import google_search
from src.services.searchServices.baiduService import baidu_search
from src.config.searchs import SearchStrategy


def search_service(query: str, method=SearchStrategy.GOOGLESEARCH.value, num_results: int = 5):
    """
    选择不同的信息检索方法
    :param query        : (str) 搜索关键词。
    :param method:      : (int) 选择的搜索方案
    :param num_results  : (int) 返回的搜索结果数量（默认 5 条）。
    :return             : (str) 格式化后的搜索结果文本或错误信息。
    """
    if method == SearchStrategy.BAIDUSEARCH.value:
        result = baidu_search(query, num_results)
    else:
        result = google_search(query, num_results)

    return result


def search_client_init():
    """
    初始化各个搜索方法访问(包括Google CSE的API、CX的设置)
    :return: (bool) 是否成功初始化
    """
    from src.config import apis

    from src.services.searchServices import googleService
    googleService.API_KEY = apis.GOOGLE_CSE_API
    googleService.CX = apis.GOOGLE_CSE_CX

    # baidu_search init to be added

    return True


if __name__ == '__main__':
    code = 0
