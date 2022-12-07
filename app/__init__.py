# -*- coding: utf-8 -*-
import logging
import logging.config

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config, logger_conf

# 由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数。

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_name):
    """
    工厂函数
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)  # 通过config.py统一接口
    register_plugins(app)
    register_shell_context(app)
    register_restful_apis(app)
    register_blueprints(app)

    # logging config
    logging.config.dictConfig(logger_conf)

    # 设置登录安全级别
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    # 配置CKEditor
    app.config['CKEDITOR_SERVE_LOCAL'] = True  # 使用CKEditor本地资源
    app.config['CKEDITOR_PKG_TYPE'] = 'basic'  # 3种类型：basic, standard and full
    app.config['CKEDITOR_LANGUAGE'] = 'zh'  # CKEditro 语言
    app.config['CKEDITOR_ENABLE_CODESNIPPET '] = True  # 代码高亮
    app.config['CKEDITOR_FILE_UPLOADER'] = '/media'  #
    app.config['CKEDITOR_ENABLE_CSRF'] = False  # 禁用CSRF保护
    csrf.init_app(app)
    # 配置分页
    app.config['POST_PER_PAGE'] = 10

    return app


# 注册插件扩展
def register_plugins(app):
    mail.init_app(app)
    db.init_app(app)


# 注册日志处理函数
def register_logging(app):
    pass


# 注册蓝图
def register_blueprints(app):
    from app.views.admin import bp_admin
    from app.views.blog import bp_blog

    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_blog)


# 注册restful API
def register_restful_apis(app):
    from app.api.v1 import api, registerResources
    registerResources()
    api.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        from app.models.category import Category
        from app.models.comment import Comment
        from app.models.page import Page
        from app.models.post import Post
        from app.models.site import Site
        from app.models.tag import Tag
        from app.models.user import User, Role
        return dict(app=app, db=db, User=User, Role=Role, Post=Post, Category=Category, Page=Page, Tag=Tag,
                    Comment=Comment, Site=Site)


# 模板上下文处理函数
def register_template_context(app):
    pass
