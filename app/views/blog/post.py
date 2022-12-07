# -*- coding: utf-8 -*-
# File: post_resource.py
# Author: Zhangzhijun
# Date: 2021/2/13 17:30
from flask import render_template

from app.views.blog import bp_blog


@bp_blog.route('/post')
def blog_post():
    return render_template('blog/post.html')
