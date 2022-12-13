# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response,redirect

route_www_guestbook = Blueprint('www_guestbook_page', __name__)

@route_www_guestbook.route("/")
def index():
    return render_template( "www/guestbook/index.html")



@route_www_guestbook.route("/post",methods=[ "POST"])
def post():
    return render_template( "www/guestbook/post.html")