# -*- coding: utf-8 -*-
# File: __init__.py.py
# Author: Zhangzhijun
# Date: 2021/2/12 18:32

from flask import Blueprint

bp_admin = Blueprint('bp_admin', __name__, url_prefix='/admin', template_folder='../templates/admin/',
                     static_folder='../static')

from .index import *
from .user import *
from .category import *
from .post import *
from .tag import *
from .page import *
from .comment import *
from .media import *
from .site import *
from .about import *
