# -*- coding: utf-8 -*-
# File: user.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:26
from flask import flash, redirect, url_for, render_template, current_app, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from app import db, login_manager
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.user_form import LoginForm, RegisterForm, UserForm
from app.models.user import User, Role
from app.utils import query_to_dict
from app.views.admin import bp_admin


@bp_admin.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = get_user_info(register_form)
        if User.query.filter_by(User.username == user.username).count() > 0:
            flash('Username has exist.', 'failed')
            current_app.logger.debug("%s has has exist.", user.username)
            return render_template('admin/register.html', register_form=register_form)
        elif User.query.filter_by(User.email == user.email).count() > 0:
            flash('Email has exist.', 'failed')
            current_app.logger.debug("%s has has exist.", user.email)
            return render_template('admin/register.html', register_form=register_form)
        else:
            db.session.add(user)
            db.session.commit()
            flash('register success!')
            current_app.logger.debug("register success.")
            return redirect(url_for('bp_admin.index'))

    return render_template('admin/register.html', register_form=register_form)


@bp_admin.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username, password=password).first()
        # 验证用户名和密码是否一致
        # if username == user.username and user.validate_password(password):
        if user:
            login_user(user)  # 登入用户
            flash('Login success.')
            current_app.logger.debug("Login success.")
            return redirect(url_for('bp_admin.index'))
        else:
            current_app.logger.debug("Login failed.")
            return redirect(url_for('bp_admin.login'))
    return render_template('admin/login.html', login_form=login_form)


@bp_admin.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    current_app.logger.debug("Logout.")
    return redirect(url_for('index'))  # 重定向回首页


@bp_admin.route('/user/list', methods=['GET'])
def admin_users_view():
    return render_template('admin/user/user.html')


@bp_admin.route('/user', methods=['GET', 'Post'])
def create_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = get_user_info(user_form)
        db.session.add(user)
        db.session.commit()
        flash('user created.', 'success')
        return redirect(url_for('bp_admin.admin_users_view'))
    return render_template('admin/Page/Page-new.html', page_form=user_form)


@bp_admin.route('/users', methods=['GET', 'Post'])
def get_users():
    try:
        users = User.query(User.id, User.username, User.nickname, Role.code, User.email, User.registertime,
                           User.status) \
            .filter(User.roleid == Role.id) \
            .all()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if users is None:
        return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(users))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/user/<string:username>', methods=['GET'])
def get_user_by_name(username):
    try:
        user = User.query(User.id, User.username, User.nickname, Role.code, User.email, User.registertime,
                          User.status) \
            .filter(User.username == username) \
            .filter(User.roleid == Role.id) \
            .first()
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if user is None:
        return jsonify(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)
    data = dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(user))
    current_app.logger.debug("data: %s", data)
    return jsonify(data)


@bp_admin.route('/user', methods=['PUT'])
def update_user(user):
    try:
        u = User.query.filter_by(username=user.username).first()
    except:
        return dict(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if u is None:
        return dict(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

    u.username = user.username,
    u.nickname = user.nickname,
    u.email = user.email

    db.session.commit()
    data = dict(code=ResponseCode.UPDATE_USER_SUCCESS, message=ResponseMessage.UPDATE_USER_SUCCESS)
    return jsonify(data)


@bp_admin.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
    except:
        return dict(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if user is None:
        return dict(code=ResponseCode.USER_NOT_EXIST, message=ResponseMessage.USER_NOT_EXIST)

    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'success')

    date = dict(code=ResponseCode.DELETE_USER_SUCCESS, message=ResponseMessage.DELETE_USER_SUCCESS)
    return jsonify(date)


# 从表单中获取post信息
def get_user_info(form):
    username = form.username.data
    nickname = form.nickname.data
    password = form.password.data
    email = form.email.data
    print(generate_password_hash(password))
    user = User(
        username=username,
        nickname=nickname,
        password_hash=generate_password_hash(password),
        email=email,
    )

    return user


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象
