# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect

route_www_food = Blueprint('www_food_page', __name__)

@route_www_food.route("/")
def index():
    return render_template( "www/food/index.html")



@route_www_food.route("/post",methods=["GET" ,"POST"])
def post():
    return render_template( "www/food/post.html")