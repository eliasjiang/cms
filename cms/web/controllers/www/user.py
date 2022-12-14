# -*- coding: utf-8 -*-
from flask import current_app, Blueprint,render_template,request,  make_response,redirect, url_for,flash, abort
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from web.models.user import User
from common.models.gym.Customer import Customer
from common.models import db
from werkzeug.security import generate_password_hash
from common.services.GlobalUrlService import GlobalUrlService

route_www_user = Blueprint('www_user_page', __name__)

"""
 Customer.query.filter_by(username=email).update({
                "password_hash": generate_password_hash("123456")
            })
            db.session.commit()

"""

@route_www_user.route("/sign-in.html",methods=["GET" ,"POST"])
def sign_in():

    if request.method == "POST":
        email = request.form['username']
        password = request.form['password']

        customer = User.get_by_account(email)
        if customer is None:
            flash('用户邮箱错误')
        else:
            user = User(customer)

            if user.verify_password(password):
                login_user(user)  # 创建用户 Session
                response = make_response(redirect(GlobalUrlService.buildWWWUrl("/account/index")))
                return response
            else:
                flash('用户密码错误！')

    return render_template( "www/user/sign-in.html")



@route_www_user.route("/sign-up.html",methods=["GET" ,"POST"])
def sign_up():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        customer = User.get_by_account(email)
        if customer is not None:
            flash('用户邮箱已经注册，请更换邮箱注册或者找回密码')
        else:

            customer = User.get_by_account(username)

            if customer is not None:
                flash('用户名已经注册，请更换用户名注册或者找回密码')
            else:
                customer = Customer()
                customer.email = email
                customer.username = username
                customer.password_hash = generate_password_hash(password)
                db.session.add(customer)
                db.session.commit()

                response = make_response(redirect(GlobalUrlService.buildWWWUrl("/account/index")))
                return response


    return render_template( "www/user/sign-up.html")

@login_required
@route_www_user.route("/logout",methods=["GET"])
def logout():
    logout_user()
    response = make_response(redirect(GlobalUrlService.buildWWWUrl("/")))
    return response


@route_www_user.route("/forgot.html",methods=["GET" ,"POST"])
def forgot():
    if request.method == "POST":
        username = request.form['username']

        customer = User.get_by_account(username)
        if customer is None:
            flash('用户邮箱或者用户名没有注册，请更换邮箱注册找回密码')
        else:
            flash('我们已经发送邮件到你的邮箱！')

            response = make_response(redirect(GlobalUrlService.buildWWWUrl("/account/index")))
            return response

    return render_template( "www/user/forgot.html")