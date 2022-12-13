# coding: utf-8
from common.models import db

class FoodCategory(db.Model):
    __tablename__ = 'food_category'
    id = db.Column(db.Integer, primary_key=True, info='目录ID')
    parent_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='上级目录ID')
    name = db.Column(db.String(120), nullable=False, server_default=db.FetchedValue(), info='目录名')
    description = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='目录描述')
    sort_num = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='目录排序号')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
                
    def setAttrs(self,items:dict):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        