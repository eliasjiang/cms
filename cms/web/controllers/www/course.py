# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect

route_www_course = Blueprint('www_course_page', __name__)

@route_www_course.route("/")
def index():
    return render_template( "www/course/index.html")



@route_www_course.route("/detail.html",methods=["GET" ,"POST"])
def post():
    return render_template( "www/course/detail.html")