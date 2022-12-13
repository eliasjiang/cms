# coding: utf-8
from common.models import db

class Subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column(db.Integer, primary_key=True, info='ID')
    customer_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='客户ID')
    plan_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='计划ID')
    charge = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='收取费用')
    status = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='状态')
    is_renewed = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否续订')
    start_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='开始时间')
    end_date = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='结束时间')
    created_at = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    updated_at = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='更改时间')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
                
    def setAttrs(self,items:dict):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        