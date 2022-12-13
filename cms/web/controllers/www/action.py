# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect

route_www_action = Blueprint('www_action_page', __name__)

@route_www_action.route("/")
def index():
    return render_template( "www/action/index.html")



@route_www_action.route("/detail.html",methods=["GET" ,"POST"])
def post():
    return render_template( "www/action/detail.html")