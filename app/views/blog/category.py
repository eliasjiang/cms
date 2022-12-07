# -*- coding: utf-8 -*-
# File: category_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:29
from flask import render_template

from app.views.blog import bp_blog


@bp_blog.route('/category')
def blog_category():
    return render_template('blog/category.html')
