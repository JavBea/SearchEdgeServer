#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :functioncall_methods.py
# @Time      :2025/1/19 16:11
# @Author    :Shao YiHan

import spacy
from collections import Counter

# 加载spaCy的英文模型
nlp = spacy.load("en_core_web_sm")


# 提取实体并计算频率的函数
def __extract_entities__(text: str):
    """
    提取一段文本中的实体词
    :param text : (str) 源文本
    :return     : 实体字典
    """
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    print(entities)
    return Counter(entities)


# 计算可靠性评分的函数
def calculate_reliability(reference, candidate):
    # 提取并计算实体频率
    ref_entity_counts = __extract_entities__(reference)
    cand_entity_counts = __extract_entities__(candidate)

    # 计算实体的加权匹配度
    total_ref_entities = sum(ref_entity_counts.values())
    total_cand_entities = sum(cand_entity_counts.values())

    matching_score = 0
    for entity, ref_count in ref_entity_counts.items():
        cand_count = cand_entity_counts.get(entity, 0)
        matching_score += min(ref_count, cand_count)

    # 计算标准化的可靠性评分（百分制）
    # 评分基于实体的匹配数量以及实体在文本中的频率
    reliability_score = (matching_score / total_ref_entities) * 100
    return reliability_score


if __name__ == '__main__':
    # 示例
    reference_text = """
    Albert Einstein was a theoretical physicist who developed the theory of relativity.
    He was awarded the Nobel Prize in Physics in 1921 for his discovery of the photoelectric effect.
    Artificial Intelligence (AI) and Machine Learning are rapidly evolving fields.
    """

    candidate_text = """
    Albert Einstein's discoveries laid the foundation for modern physics.
    He was a Nobel laureate, recognized for his contributions to science.
    AI and Machine Learning are part of the ongoing technological revolution.
    """

    # 计算candidate的可靠性评分
    reliability = calculate_reliability(reference_text, candidate_text)
    print(f"Candidate's Reliability Score: {reliability:.2f}%")
