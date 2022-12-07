# -*- coding: utf-8 -*-
# File: __init__.py.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:32
from flask import Blueprint

bp_blog = Blueprint('bp_blog', __name__, template_folder='../templates/blog', static_folder='../static')

from .category import *
from .index import *
from .post import *
from .page import *
