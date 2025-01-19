#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :searchs.py
# @Time      :2025/1/19 10:16
# @Author    :Shao YiHan
from enum import Enum, auto


class SearchStrategy(Enum):
    # 谷歌搜索方案
    GOOGLESEARCH = auto()
    # 百度+爬虫搜索方案
    BAIDUSEARCH = auto()


if __name__ == '__main__':
    codes = 0
