# _*_ coding:utf-8 -*-
# File: tag.py
# Version: v1.0.0
# Author: Zhang Zhijun
# Date: 2022/8/26 21:22
# License: MulanPSL2
from flask import render_template

from app.views.admin import bp_admin


@bp_admin.route('/tag/list')
def admin_tag_view():
    return render_template('admin/post/tag.html')


@bp_admin.route('/tags')
def get_tags():
    pass


@bp_admin.route('/tags/<int:post_id>')
def get_tags_by_id():
    pass


@bp_admin.route('/tags/post/<int:post_id>')
def get_tags_by_postid():
    pass
