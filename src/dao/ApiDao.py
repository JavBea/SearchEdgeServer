#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ApiDao.py
# @Time      :2025/1/12 11:12
# @Author    :Shao YiHan
from src.services.dbService import db
from src.models.api import Api
from sqlalchemy.exc import SQLAlchemyError
import app


class ApiDao:

    @staticmethod
    def create_api(name, api_key, other):
        """
        创建新的 API 记录
        :param name: API名称
        :param api_key: API_key
        :param other: API的其他字段
        :return:
        """
        new_api = Api(api_name=name, api_key=api_key, other=other)
        try:
            db.session.add(new_api)
            db.session.commit()
            return new_api
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_api_by_name(name):
        """
        根据名称查询 API
        :param name: 用于查询的API名称
        :return: api_key
        """
        return Api.query.filter_by(api_name=name).first()

    @staticmethod
    def update_api_file():
        """
        更新src/config/api.py中的api变量以供使用
        :return: (bool) 是否成功更新api变量
        """
        from src.config import apis
        apis.GPT_API = ApiDao.get_api_by_name('chatgpt').api_key
        apis.QWEN_API = ApiDao.get_api_by_name('qwen').api_key
        apis.GOOGLE_CSE_API = ApiDao.get_api_by_name('google').api_key
        apis.GOOGLE_CSE_CX = ApiDao.get_api_by_name('google').other


if __name__ == '__main__':
    service = ApiDao()
    print(service.get_api_by_name('chatgpt').str())
    code = 0
