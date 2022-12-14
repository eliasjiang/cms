# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,make_response, request, redirect, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from common.services.GlobalUrlService import GlobalUrlService
from common.models.gym.Customer import Customer
from common.models import db
from werkzeug.security import generate_password_hash

route_www_account = Blueprint('www_account_page', __name__)

@login_required
@route_www_account.route("/index")
def index():
    response = make_response(redirect(GlobalUrlService.buildWWWUrl("/account/profile.html")))
    return response
    #return render_template( "www/account/index.html")


@login_required
@route_www_account.route("/profile.html",methods=["GET" ,"POST"])
def profile():
    user = current_user._get_current_object()
    customer = Customer.query.filter_by(id=user.id).first()

    if request.method == "POST":
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        name = request.form['name'].strip()
        mobile = request.form['mobile'].strip()
        address = request.form["address"].strip()
        city = request.form["city"].strip()
        province = request.form["province"].strip()

        Customer.query.filter_by(id=user.id).update({
            "email":email,
            "username": username,
            "name": name,
            "mobile": mobile,
            "city": city,
            "province":province,
            "address": address,

        })
        db.session.commit()

        flash('个人信息已经保存！')

    return render_template("www/account/profile.html", customer=customer)



@login_required
@route_www_account.route("/password.html",methods=["GET" ,"POST"])
def password():
    user = current_user._get_current_object()

    if request.method == "POST":
        password = request.form['password'].strip()
        newpassword = generate_password_hash(password)

        Customer.query.filter_by(id=user.id).update({
            "password_hash": newpassword,
        })
        db.session.commit()
        flash('新密码已经保存！')

    return render_template("www/account/password.html")


@login_required
@route_www_account.route("/favorite.html",methods=["GET" ])
def favorite():
    return render_template( "www/account/favorite.html")


@login_required
@route_www_account.route("/subscription.html",methods=["GET" ])
def subscription():
    return render_template( "www/account/subscription.html")