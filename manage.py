# -*- coding: utf-8 -*-

import os

from flask_migrate import Migrate

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
# migrate = Migrate(app, db)
Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role, Post=Post, Category=Category, Page=Page, Tag=Tag, Comment=Comment,
#                 Site=Site)


if __name__ == '__main__':
    app.run()
