# coding: utf-8
from common.models import db

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, info='ID')
    name = db.Column(db.String(180), nullable=False, server_default=db.FetchedValue(), info='课程名称')
    cover = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='封面')
    video = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='视频')
    description = db.Column(db.Text, info='描述')
    part = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='部位')
    difficult = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue(), info='难度')
    tags = db.Column(db.String(250), nullable=False, server_default=db.FetchedValue(), info='标签')
    status = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue(), info='状态')
    created_at = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    upated_at = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='更改时间')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
                
    def setAttrs(self,items:dict):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
        