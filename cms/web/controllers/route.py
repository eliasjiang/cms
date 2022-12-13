# -*- coding: utf-8 -*-
from application import  app
from common.components.helper.UtilHelper import UtilHelper

'''
蓝图功能，对所有的url进行蓝图功能配置
'''

from web.controllers.www.index import route_www_index
from web.controllers.www.guestbook import route_www_guestbook
from web.controllers.www.tools import route_www_tools
from web.controllers.www.food import route_www_food
from web.controllers.www.course import route_www_course
from web.controllers.www.action import route_www_action
from web.controllers.www.user import route_www_user
from web.controllers.www.account import route_www_account

from web.controllers.static import route_static
from web.controllers.admin.tools.gii.index import route_home_gii
from web.controllers.admin.error.index import route_home_error
from web.controllers.admin.index import route_home_index
from web.controllers.admin.user.User import route_home_user
from web.controllers.admin.user.Profile import route_home_profile
from web.controllers.admin.rbac.staff import route_home_staff
from web.controllers.admin.rbac.dept import route_home_dept
from web.controllers.admin.rbac.grant import route_home_grant
from web.controllers.admin.log.log import route_home_log
from web.controllers.admin.link.index import route_home_link
from web.controllers.admin.oauth.index import route_home_oauth_index

MODULES = (
    ( route_www_index, '/' ),
    (route_www_guestbook, "/guestbook"),
    (route_www_tools, "/tools"),
    (route_www_food, "/food"),
    (route_www_course, "/course"),
    (route_www_action, "/action"),
    (route_www_user, "/user"),
    (route_www_account, "/account"),
    ( route_static, '/static' ),
    ( route_home_index, '/admin' ),
    ( route_home_error, '/admin/error' ),
    ( route_home_log, '/admin/log' ),
    ( route_home_staff, '/admin/rbac/staff' ),
    ( route_home_dept, '/admin/rbac/dept' ),
    ( route_home_grant, '/admin/rbac/grant' ),
    ( route_home_link, '/admin/link' ),
    ( route_home_user, '/admin/user' ),
    ( route_home_profile, '/admin/profile' ),
    ( route_home_oauth_index, '/admin/oauth' ),
)


def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)


if not UtilHelper.isProdEnv():
    DEV_TOOLS_MODULES = (
        (route_home_gii, '/admin/tools/gii'),
    )
    setting_modules(app, DEV_TOOLS_MODULES)