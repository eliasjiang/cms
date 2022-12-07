#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0.0
# author:Zhang Zhijun
# time: 2021-03-13
# file: category_resource.py
# function:
# modify:
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField('分类名称', validators=[Length(min=1, max=65, message='标题长度为1~64位'), DataRequired(message='标题不能为空')])
    slug = StringField('分类别名', validators=[Length(min=1, max=65, message='别名长度为6~12位'), DataRequired(message='别名不能为空')])
    # parentid = SelectField('父分类', validators=[DataRequired()])
    description = StringField('分类描述', validators=[Length(min=1, max=65, message='描述长度为1-64位')])

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        # self.parentid.choices = [(category.id, category.name)
        #                          for category in Category.query.order_by(Category.name).all()]

    # 把SQLAlchemy查询对象转换成字典
    # def to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
