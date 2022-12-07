# -*- coding: utf-8 -*-
# File: user_resource.py
# Author: Zhangzhijun
# Date: 2021/2/12 22:43
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, Email, ValidationError

from app.models.user import Role, User


class UserForm(FlaskForm):
    username = StringField(u'用户名',
                           validators=[Length(min=1, max=64, message='账号长度为1~64位'), DataRequired(message='用户名不能为空')])
    nickname = StringField(u'昵称',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    password = PasswordField(u'密码',
                             validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空')])
    email = StringField(u'邮箱',
                        validators=[Length(min=8, max=128, message='邮箱长度为8~128位'), DataRequired(message='邮箱不能为空'),
                                    Email()])
    roleid = SelectField(u'角色', validators=[DataRequired()])
    status = IntegerField(u'用户状态', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.roleid.choices = [(role.id, role.name)
                               for role in Role.query.order_by(Role.name).all()]


class RegisterForm(FlaskForm):
    username = StringField(label=u'用户名',
                           validators=[Length(min=1, max=64, message='账号长度为1~64位'),
                                       DataRequired(message='用户名不能为空'), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                               '用户名只能由字母，数字，下划线和点组成，且必须以字母开头！')])
    nickname = StringField(label=u'昵称',
                           validators=[Length(min=1, max=64, message='昵称长度为1~64位'), DataRequired(message='用户别名不能为空')])
    password = PasswordField(label=u'密码',
                             validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空')])
    password2 = PasswordField(label=u'确认密码',
                              validators=[Length(min=8, max=256, message='密码长度为8~16位'), DataRequired(message='密码不能为空'),
                                          EqualTo("password", "两次密码不一致")])
    email = StringField(label=u'邮箱',
                        validators=[Length(min=8, max=128, message='邮箱长度为8~128位'), DataRequired(message='邮箱不能为空'),
                                    Email()])
    submit = SubmitField(label=u'注册')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).count() > 0:
            raise ValidationError('Email already registered')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).count() > 0:
            raise ValidationError('Username has exist')


class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
