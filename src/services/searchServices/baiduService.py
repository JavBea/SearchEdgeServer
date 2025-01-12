#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :baiduService.py
# @Time      :2025/1/12 16:10
# @Author    :Shao YiHan

from src.services.searchServices.googleService import google_search


def baidu_search(query: str, num_results: int = 5):
    """
    使用 Google Custom Search Engine API 执行搜索查询。
    :param query        : (str) 搜索关键词。
    :param num_results  : (int) 返回的搜索结果数量（默认 5 条）。
    :return             : (str)格式化后的搜索结果文本或错误信息。
    """

    return google_search(query, num_results)


if __name__ == '__main__':
    code = 0
