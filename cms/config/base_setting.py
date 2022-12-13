# -*- coding: utf-8 -*-
APP_NAME = "西大健身"
APP_VERSION = "V3.0"
SERVER_PORT = 8889
API_SERVER_PORT = 8888

'''
有可能你使用浏览器看到的一串字符串(ascii编码)不是那么容易看懂的，
这是因为python底层使用unicode编码。
通过设置下面的参数可以解决这个问题。
'''
JSON_AS_ASCII = False


DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = True
SQLALCHEMY_ECHO = False
SECRET_KEY = 'ZoDWffA2d90eVOzii'

## 域名配置
DOMAIN = {
    "www": "http://127.0.0.1:" + str( SERVER_PORT ),
    "api": "http://127.0.0.1:" + str( API_SERVER_PORT ),
    "resource" : "http://img.abc.dev"
}


##过滤url
IGNORE_URLS_HOME = [
    "^/admin/user/login",
    "^/admin/user/logout",
    "^/admin/oauth/",
]

## 权限过滤的
IGNORE_URLS_HOME_RRIVILEGE = [
    "^/admin/error",
    "^/admin/profile",
]


IGNORE_URLS_WWW = [
]

##登录忽略url
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

##HTTP请求超时时间
HTTP_TIMEOUT = 5

##日志存放位置 一定不能放在tmp目录 tmp有自己的回收机制了
LOG_ROOT_PATH = "/data/www/logs/cms"
##版本号文件
RELEASE_PATH = "/data/www/release_version/cms"

