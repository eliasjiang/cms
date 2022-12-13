# coding: utf-8
from common.models import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True, info='用户ID')
    email = db.Column(db.String(120), nullable=False, server_default=db.FetchedValue(), info='用户邮箱(账号)')
    username = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='用户名')
    password_hash = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='用户密码(加密字符串)')
    name = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='客户姓名')
    address = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='用户地址')
    city = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='城市或县')
    province = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='省')
    mobile = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='手机号码')
    balance = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='账户余额')
    credit_level = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='信用等级 一级为10%的折扣，不能透支；二级为15%的折扣，不能透支；三级为15%的折扣，透支有额度限制；四级为20%的折扣，透支有额度限制；五级为25%的折扣')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
                
    def setAttrs(self,items:dict):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        