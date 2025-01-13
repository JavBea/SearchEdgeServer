#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :UserService.py
# @Time      :2025/1/13 17:07
# @Author    :Shao YiHan
from typing import Optional

from src.services.dbService import db
from src.models.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        """
        根据用户ID获取用户。
        :param user_id: 用户ID
        :return: User对象或None
        """
        try:
            return User.query.filter_by(user_id=user_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_user_by_name(user_name: str) -> User:
        """
        根据用户名获取用户。
        :param user_name: 用户名
        :return: User对象或None
        """
        try:
            return User.query.filter_by(user_name=user_name).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_user_by_email(email: str) -> User:
        """
        根据用户绑定的电子邮箱获取用户。
        :param email: 用户邮箱
        :return: User对象或None
        """
        try:
            return User.query.filter_by(email=email).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def check_user(check_token: str, password: str):
        """
        登录时检查用户输入的账密
        :param check_token: 登录时输入的用户名或绑定的邮箱
        :param password: 登录时输入的密码
        :return: 登录成功返回用户对象否则返回None,返回响应码code=2001(登录成功),code=2002(登录失败)
        """
        try:
            user = User.query.filter_by(email=check_token).first()
            if user is None:
                user = User.query.filter_by(user_name=check_token).first()
                if user is None:
                    return None, "2002"

            if user.password == password:
                return user, "2001"
            else:
                return None, "2002"

        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_all_users() -> list[User]:
        """
        获取所有用户。
        :return: 用户对象列表
        """
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def create_user(password: str, role: str = 'user', user_name: str = None, email: str = None):
        """
        创建一个新用户。
        :param password: 用户密码
        :param role: 用户角色（'user' 或 'admin'）
        :param user_name: 用户名
        :param email: 用户邮箱
        :return: 新创建的User对象, 注册响应码code：code=1001(注册成功),code=1002(用户名已被占用),
                code=1003(邮箱已被占用),code=1004(密码格式错误),code=1005(邮箱格式错误)
        """

        # 如果用户名已被占用
        if UserService.get_user_by_name(user_name) is not None:
            code = "1002"
            return None, code

        # 如果邮箱已被占用
        if UserService.get_user_by_email(email) is not None:
            code = "1003"
            return None, code

        from src.utils import password_checker

        # 检查密码是否符合要求
        if not password_checker.is_valid_password(password):
            code = "1004"
            return None, code

        from src.utils import email_checker

        # 检查邮箱格式是否正确
        if not email_checker.is_valid_email(email):
            code = "1005"
            return None, code

        new_user = User(password=password, role=role, user_name=user_name, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            code = "1001"
            return new_user, code
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_user(user_id: int, **kwargs) -> User:
        """
        根据用户ID更新用户信息。
        :param user_id: 用户ID
        :param kwargs: 要更新的字段及其值
        :return: 更新后的User对象
        """
        user = UserService.get_user_by_id(user_id)
        if not user:
            raise ValueError("用户未找到")

        try:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)

            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """
        根据用户ID删除用户。
        :param user_id: 用户ID
        :return: 删除成功返回True，否则返回False
        """
        user = UserService.get_user_by_id(user_id)
        if not user:
            raise ValueError("用户未找到")

        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e


if __name__ == '__main__':
    codes = 0
