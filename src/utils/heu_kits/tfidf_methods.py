#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tfidf_methods.py
# @Time      :2025/1/17 11:20
# @Author    :Shao YiHan
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def tfidf_similarity_english(text1, text2, top_n=10):
    """
    使用 TF-IDF 提取关键词并计算两个 英文 文本的匹配度。
    :param text1: 第一个文本 （English）
    :param text2: 第二个文本 （English）
    :param top_n: 提取的关键词数量
    :return match_score: float, 两个文本的匹配度（百分制）
    """
    # 创建 TF-IDF 向量器
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    feature_names = vectorizer.get_feature_names_out()

    # 获取两个文本的 TF-IDF 向量
    tfidf_array = tfidf_matrix.toarray()

    # 提取每个文本的 top_n 关键词及其权重
    def extract_top_keywords(tfidf_vector, feature_names, top_n):
        sorted_indices = np.argsort(-tfidf_vector)[:top_n]
        return {feature_names[i]: tfidf_vector[i] for i in sorted_indices}

    keywords1 = extract_top_keywords(tfidf_array[0], feature_names, top_n)
    keywords2 = extract_top_keywords(tfidf_array[1], feature_names, top_n)

    print("Text 1 Keywords:", keywords1)
    print("Text 2 Keywords:", keywords2)

    # 计算关键词交集的加权得分
    intersection = set(keywords1.keys()) & set(keywords2.keys())
    if not intersection:
        return 0.0  # 无交集，匹配度为0

    # 计算匹配得分（关键词交集中，权重乘积的平均值）
    similarity_score = sum(keywords1[word] * keywords2[word] for word in intersection)
    max_score = np.sqrt(sum(value ** 2 for value in keywords1.values())) * \
                np.sqrt(sum(value ** 2 for value in keywords2.values()))

    match_score = (similarity_score / max_score) * 100 if max_score != 0 else 0
    return round(match_score, 2)


def tfidf_similarity_chinese(text1, text2, top_n=10):
    """
    使用 TF-IDF 提取关键词并计算两个 中文 文本的匹配度。
    :param text1: 第一个文本 （English）
    :param text2: 第二个文本 （English）
    :param top_n: 提取的关键词数量

    :return match_score: float, 两个文本的匹配度（百分制）
    """
    # code here


if __name__ == '__main__':
    # 示例文本
    text10 = "The sun rises in the east and sets in the west. The earth revolves around the sun."
    text20 = "The earth revolves around the sun, and the sun sets in the west."

    # 计算匹配度
    match_score = tfidf_similarity_english(text10, text20)
    print(f"Matching Score: {match_score}/100")
    codes = 0
