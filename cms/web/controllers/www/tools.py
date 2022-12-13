# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect

route_www_tools = Blueprint('www_tools_page', __name__)

@route_www_tools.route("/")
def index():
    return render_template( "www/tools/index.html")

