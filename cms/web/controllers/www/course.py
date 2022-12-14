# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,make_response,redirect
from common.models.gym.Course import Course
from common.components.helper.DateHelper import DateHelper
from common.components.helper.UtilHelper import UtilHelper
from common.services.CommonConstant import CommonConstant


route_www_course = Blueprint('www_course_page', __name__)

@route_www_course.route("/")
def index():
    req = request.values
    page = int(req.get("p", 1))

    category_ids = req['category_ids'].split(",") if ('category_ids' in req and req['category_ids']) else []

    query = Course.query.filter_by(Course.status == 1)
    if len(category_ids) > 0:
        query.filter_by(Course.category_id.in_(category_ids))


    page_params = {
        "total": query.count(),
        "page_size": CommonConstant.PAGE_SIZE,
        "page": page,
        "display": CommonConstant.PAGE_DISPLAY,
    }

    pages = UtilHelper.iPagination(page_params)
    offset = (page - 1) * CommonConstant.PAGE_SIZE
    limit = CommonConstant.PAGE_SIZE * page
    list = query.order_by(Course.id.desc())[offset:limit]

    return render_template( "www/course/index.html",{"list": list,"pages":pages })



@route_www_course.route("/detail.html",methods=["GET" ,"POST"])
def post():
    return render_template( "www/course/detail.html")