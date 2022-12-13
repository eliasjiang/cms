# coding: utf-8
from common.models import db

class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True, info='ID')
    name = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='训练计划名称')
    description = db.Column(db.Text, info='详情')
    course_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='课程ID')
    charge = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='收取费用')
    status = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='状态')
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
        