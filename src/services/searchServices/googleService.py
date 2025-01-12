#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :googleService.py
# @Time      :2025/1/8 10:34
# @Author    :Shao YiHan
import requests

API_KEY = None
CX = None


def google_search(query: str, num_results: int = 5):
    """
    使用 Google Custom Search Engine API 执行搜索查询。
    :param query        : (str) 搜索关键词。
    :param num_results  : (int) 返回的搜索结果数量（默认 5 条）。
    :return             : (str)格式化后的搜索结果文本或错误信息。
    """

    # Google CSE API 的请求 URL
    base_url = "https://www.googleapis.com/customsearch/v1"

    # 请求参数
    params = {
        "q": query,  # 搜索的关键词
        "key": API_KEY,  # 全局 API 密钥
        "cx": CX,  # 全局 Custom Search Engine ID
        "num": num_results  # 返回的搜索结果数量
    }

    try:
        # 发起 HTTP 请求
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # 检查是否返回 HTTP 错误
        data = response.json()  # 将响应转换为 JSON

        # 解析并格式化搜索结果
        results = data.get("items", [])
        if not results:
            return "No results found for the given query."

        # 构造结果字符串
        formatted_results = []
        for item in results:
            # title = item.get("title", "No Title")
            # link = item.get("link", "No Link")
            snippet = item.get("snippet", "No Snippet")
            formatted_results.append(f"{snippet}")

        # 将结果合并为一个字符串
        return "\n".join(formatted_results)

    except requests.exceptions.RequestException as e:
        # 捕获 HTTP 请求的异常
        return f"Error during Google CSE search: {e}"

    except KeyError:
        # 捕获 JSON 解析中的异常
        return "Unexpected response format from Google CSE API."


if __name__ == '__main__':
    aquery = "Who won the 2024 US presidential election?"
    result = google_search(query=aquery, num_results=3)
    print(result)
