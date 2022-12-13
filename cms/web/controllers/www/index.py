# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect
from application import app
import math
from common.models.link.Link import Link
from common.services.CommonConstant import CommonConstant
from common.services.GlobalUrlService import GlobalUrlService
from common.components.helper.ConfigHelper import ConfigHelper

route_www_index = Blueprint('www_index_page', __name__)

@route_www_index.route("/")
def index():
    return render_template( "www/index/index.html" )

@route_www_index.route("/about.html")
def about():
    return render_template("www/index/about.html")

@route_www_index.route("/contact.html")
def contact():
    return render_template("www/index/contact.html")