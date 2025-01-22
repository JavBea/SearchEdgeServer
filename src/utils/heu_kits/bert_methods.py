#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :bert_methods.py
# @Time      :2025/1/17 19:24
# @Author    :Shao YiHan

from sentence_transformers import SentenceTransformer, util

# 加载预训练的Sentence-BERT模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def bert_similarity(reference, candidate):
    """
    使用 BERT的 paraphrase-MiniLM-L6-v2模型来实现句子级别的语义匹配
    :param reference: (str) 参考文本
    :param candidate: (str) 待测文本
    :return         : (float) 相似度
    """
    # 编码为向量
    reference_embedding = model.encode(reference, convert_to_tensor=True)
    candidate_embedding = model.encode(candidate, convert_to_tensor=True)

    # 计算余弦相似度
    similarity = util.pytorch_cos_sim(reference_embedding, candidate_embedding).item()

    # 转为百分制
    similarity *= 100
    print(f"Sentence-BERT Semantic Similarity: {similarity}")

    return similarity


if __name__ == '__main__':
    reference0 = ("I am an AI language model created by OpenAI, designed to assist with providing information and "
                  "answering questions on a wide range of topics. How can I help you today?")
    candidate0 = ("I am an AI language model created by OpenAI, designed to assist with providing information, "
                  "answering questions, and performing various tasks to the best of my abilities within the scope of "
                  "my programming and training. If you have any questions or need assistance, feel free to ask!")
    print(bert_similarity(reference0, candidate0))
    codes = 0
