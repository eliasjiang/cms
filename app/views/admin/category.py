#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version: 1.0.0
# File: category_resource.py
# Author:Zhang Zhijun
# Time: 2021-03-13

from flask import render_template, jsonify, url_for, current_app
from werkzeug.utils import redirect

from app import db
from app.errors.errorcode import ResponseCode, ResponseMessage
from app.forms.category_form import CategoryForm
from app.models.category import Category
from app.models.post import Post
from app.utils import query_to_dict
from app.views.admin import bp_admin
from app.views.common.category_resource import CategoryResource


@bp_admin.route('/category/list', methods=['GET'])
def admin_category():
    return render_template('admin/category/category.html')


@bp_admin.route('/category', methods=['GET', 'POST'])
def create_category():
    current_app.logger.debug("Enter function create_category...")
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        category = get_category_info(category_form)
        current_app.logger.debug("category: %s", category)
        if (Category.query.filter_by(slug=category.slug).count() > 0) or (
                Category.query.filter_by(name=category.name).count() > 0):
            current_app.logger.debug("category already exist!")
            return dict(code=ResponseCode.CATEGORY_ALREADY_EXIST, message=ResponseMessage.CATEGORY_ALREADY_EXIST)
        db.session.add(category)
        db.session.commit()
        current_app.logger.debug("insert category to db success!")
        return dict(code=ResponseCode.SUCCESS, message=ResponseMessage.SUCCESS, data=query_to_dict(category))

    return render_template('admin/category/category-new.html', category_form=category_form)


@bp_admin.route('/categories', methods=['GET'])
def get_categories():
    current_app.logger.debug("Enter function get_categories...")
    data = CategoryResource.query_categories()
    return jsonify(data)


@bp_admin.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    data = CategoryResource.query_category_by_id(category_id)
    current_app.logger.debug("data: %s", data)
    return data


@bp_admin.route('/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category_form = CategoryForm()
    try:
        category = Category.query.get_or_404(category_id)
    except:
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if category is None:
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    if category_form.validate_on_submit():
        category = get_category_info(category_form)
        db.session.add(category)
        db.session.commit(category)
        return redirect(url_for('bp_admin.get_categories'))

    category_form.title.data = category.title
    category_form.slug.data = category.slug
    category_form.description.data = category.description

    return render_template('admin/category/category-edit.html', category_form=category_form)


@bp_admin.route('/category/<int:category_id>', methods=['Delete'])
def delete_category(category_id):
    if category_id == 1:
        current_app.logger.debug("default category, can not be deleted!")
        return
    try:
        category = Category.query.filter_by(id=category_id).first()
    except:
        current_app.logger.debug("query db filed")
        return jsonify(code=ResponseCode.QUERY_DB_FAILED, message=ResponseMessage.QUERY_DB_FAILED)
    if category is None:
        current_app.logger.debug("the category doesn't exist!")
        return jsonify(code=ResponseCode.CATEGORY_NOT_EXIST, message=ResponseMessage.CATEGORY_NOT_EXIST)

    # 默认分类不能删除
    if category.name == "未分类":
        current_app.logger.debug("default category, can not be deleted!")
        return jsonify(code=ResponseCode.CATEGORY_IS_DEFAULT_CATEGORY,
                       message=ResponseMessage.CATEGORY_IS_DEFAULT_CATEGORY)
    # 关联文章不能删除
    count = Post.query.filter.filter_by(category_id=category_id).count()
    if count == 0:
        db.session.delete(category)
        db.session.commit()
    else:
        current_app.logger.debug("the category associate with the posts, can not be deleted!")
        return jsonify(code=ResponseCode.CATEGORY_ASSOCIATE_WITH_POST,
                       message=ResponseMessage.CATEGORY_ASSOCIATE_WITH_POST)
    current_app.logger.debug("delete category success!")
    date = dict(code=ResponseCode.DELETE_CATEGORY_SUCCESS, message=ResponseMessage.DELETE_CATEGORY_SUCCESS)
    return jsonify(date)


def get_category_info(form):
    category = Category()
    category.name = form.name.data
    category.slug = form.slug.data
    # category.parentid = form.parentid.data
    category.description = form.description.data
    current_app.logger.debug("category: %s", category)
    return category
