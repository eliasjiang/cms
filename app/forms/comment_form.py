#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: comment_form.py
# Author: Zhangzhijun
# Date: 2021/9/15 22:25
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    nickname = StringField(u'昵称',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    content = StringField('内容', validators=[DataRequired(message='内容不能为空')])
    status = RadioField('状态', default=True, validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
