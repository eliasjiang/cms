# -*- coding: utf-8 -*-
# File: index.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:33
from flask import render_template

from app.views.blog import bp_blog


@bp_blog.route('/')
@bp_blog.route('/index')
def blog_index():
    return render_template('blog/index.html')
