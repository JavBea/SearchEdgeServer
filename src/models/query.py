#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :query.py
# @Time      :2025/1/18 10:46
# @Author    :Shao YiHan
class Query:
    def __init__(self, query: str, func_on: bool, llm, model, messages=None):
        self.query = query
        self.messages = messages
        self.func_on = func_on
        self.llm = llm
        self.model = model


if __name__ == '__main__':
    query0 = Query(query="aa", messages="bb", func_on=True, llm="bb", model="aa")
    print(query0.llm)
    codes = 0
