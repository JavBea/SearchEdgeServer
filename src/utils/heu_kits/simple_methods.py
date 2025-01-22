#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :simple_methods.py
# @Time      :2025/1/18 21:27
# @Author    :Shao YiHan
import re

"""
提取并验证年月份
"""

# 提取年份与月份
# 定义中文月份到英文缩写的映射
month_translation = {
    '一月': 'Jan', '二月': 'Feb', '三月': 'Mar', '四月': 'Apr', '五月': 'May', '六月': 'Jun',
    '七月': 'Jul', '八月': 'Aug', '九月': 'Sep', '十月': 'Oct', '十一月': 'Nov', '十二月': 'Dec',
    '1月': 'Jan', '2月': 'Feb', '3月': 'Mar', '4月': 'Apr', '5月': 'May', '6月': 'Jun',
    '7月': 'Jul', '8月': 'Aug', '9月': 'Sep', '10月': 'Oct', '11月': 'Nov', '12月': 'Dec'
}

# 定义英文全写月份到缩写月份的映射
month_translation_en = {
    'January': 'Jan', 'February': 'Feb', 'March': 'Mar', 'April': 'Apr', 'May': 'May', 'June': 'Jun',
    'July': 'Jul', 'August': 'Aug', 'September': 'Sep', 'October': 'Oct', 'November': 'Nov', 'December': 'Dec'
}


def __extract_year_and_month__(text):
    # 匹配年份，假设年份是四位数字
    year_pattern = r'\b\d{4}\b'
    # 匹配英文月份（包括全写月份）
    month_pattern_en = r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b'
    # 匹配中文月份（包括“2月”，“二月”）
    month_pattern_cn = r'\b(\d{1,2}月|[一二三四五六七八九十]月)\b'

    years = re.findall(year_pattern, text)
    months_en = re.findall(month_pattern_en, text)
    months_cn = re.findall(month_pattern_cn, text)

    # 将中文月份转换为英文缩写
    months_cn_translated = [month_translation[month] if month in month_translation else month for month in months_cn]

    # 将英文全写月份转换为缩写形式
    months_en_translated = [month_translation_en[month] for month in months_en]

    # 合并年份和月份，并将所有月份转换为英文缩写形式
    months_combined = months_en_translated + months_cn_translated
    combined = set(years + months_combined)

    return combined


def __yearmonth_evaluate__(reference, candidate):
    # 创建一个集合来去除重复项
    reference_set = set(reference)
    candidate_set = set(candidate)

    # 计算交集，即candidate中出现在reference中的元素
    common_elements = reference_set.intersection(candidate_set)

    # 每个共同元素加50分
    score = len(common_elements) * 50

    return score


"""
提取并验证数学等式
"""


def __extract_equations__(text):
    # 只匹配包含数字、运算符、括号和等号的部分，确保是数学公式
    pattern = r'[-+]?\d*\.\d+|\d+|[()+\-*/=]'  # 匹配数字、运算符、括号和等号
    equations = re.findall(r"(\d+[\+\-\*/\(\)]+[\d\+\-\*/\(\)]+=?[\d]*)", text)
    return equations


# 验证等式正误
def __validate_equation__(equation):
    # 以'='为分隔符分开左侧和右侧
    if '=' in equation:
        left, right = equation.split('=')
        try:
            # 计算左右两边表达式的结果
            left_result = eval(left.strip())
            right_result = eval(right.strip())
            return left_result == right_result
        except Exception as e:
            # 计算过程中出现错误，返回False
            print(f"Error evaluating equation: {e}")
            return False
    return False


"""
提供给外部的函数
"""


def search_pattern(text: str, pattern: str) -> bool:
    """
    基于KMP算法，检测文本 text 中是否含有文本 pattern
    :param text     : (str) 源文本
    :param pattern  : (str) 特征文本
    :return:
    """
    # 计算部分匹配表
    def build_partial_match_table(pattern: str):
        m = len(pattern)
        lps = [0] * m  # lps 数组用于存储每个位置的前缀匹配长度
        length = 0  # 当前最长前缀后缀长度
        i = 1  # 从第二个字符开始匹配

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # 使用已知的部分匹配信息，减少不必要的比较
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # KMP 算法
    n, m = len(text), len(pattern)
    if m == 0:
        return True  # 空的模式永远匹配
    lps = build_partial_match_table(pattern)
    i, j = 0, 0  # i 为 text 的索引，j 为 pattern 的索引

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return True  # 找到匹配
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # 跳转到 lps 数组指示的位置，避免重复比较
            else:
                i += 1
    return False  # 如果遍历结束都没有找到匹配


def extract_and_validate_equations(text):
    """
    提取并验证等式正误
    :param text : (str) 输入的文本
    :return     : (list,list) 正确的数学等式，错误的数学等式
    """
    # 首先提取等式
    equations = __extract_equations__(text)

    # 正确的等式
    valid_equations = []
    # 错误的等式
    invalid_equations = []

    # 遍历并筛选
    for eq in equations:
        if __validate_equation__(eq):
            valid_equations.append(eq)
        else:
            invalid_equations.append(eq)

    # 返回筛选后的两个集合
    return valid_equations, invalid_equations


def validate_year_and_month(refernce, candidate):
    """
    提取并验证两个文本中的年月份
    :param refernce : (str) 作为参考的文本
    :param candidate: (str) 待测文本
    :return: (int) 评测的分数
    """

    # 提取年月份
    ym_set1 = __extract_year_and_month__(refernce)
    ym_set2 = __extract_year_and_month__(candidate)

    # 如果某个文本中压根没有年月份
    if len(ym_set1) == 0 or len(ym_set2) == 0:
        return 100

    # 计算分数
    score = __yearmonth_evaluate__(ym_set1, ym_set2)

    return score


if __name__ == '__main__':
    # 提取年月份示例文本
    # text = ("The year 2023 was important, and February, 2024, followed by 5月. I also saw 2020 and 二月 "
    #         "in the same document.")
    #
    # result = __extract_year_and_month__(text)
    # print(result)

    # # 年月评估
    # reference = ['2021', '2022', 'Jan', 'Feb', 'Mar']
    # candidate = ['2022', 'Feb', 'Nov', '2021']
    # 计算评分
    # score = __yearmonth_evaluate__(result, result)
    # print(f"Score: {score}")

    # # 提取并验证公式
    # texts = "**Here**//--- are some equations: 2+3=5, 4*5-1=19, (10-3)=7"
    # valid_eqs = extract_and_validate_equations(texts)
    #
    # print("Valid equations:", valid_eqs)
    # codes = 0

    # 测试
    text = ("As of my last update in October 2023, the results of the 2024 U.S. presidential election have not yet "
            "been determined. The election is still upcoming, and the candidates, campaigns, and outcomes are subject "
            "to change. For the most current information, please follow reliable news sources or official election "
            "updates as the event approaches.")
    pattern = "last update"
    result = search_pattern(text, pattern)
    print(result)  # 输出 True

