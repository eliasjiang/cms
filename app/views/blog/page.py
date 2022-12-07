# -*- coding: utf-8 -*-
# File: page_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:29
from flask import render_template

from app.views.blog import bp_blog


@bp_blog.route('/page')
def blog_page():
    return render_template('blog/page.html')
