

from flask_login import UserMixin, LoginManager
from common.models.gym.Customer import Customer
from werkzeug.security import check_password_hash
from sqlalchemy import or_

login_manager = LoginManager()

class User(UserMixin):
    """用户类"""

    def __init__(self, user):
        self.username = user.username
        self.password_hash = user.password_hash
        self.id = user.id


    def check_account(self,name):
        customer = Customer.query.filter(or_(Customer.username == name, Customer.email == name)).first()
        if customer is None:
            return False
        else:
            return True

    def verify_password(self, password):
        """密码验证"""
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        """获取用户ID"""
        return self.id

    @staticmethod
    def get_by_account(name):

        if not name:
            return None
        customer = Customer.query.filter(or_(Customer.username == name, Customer.email == name)).first()

        if customer is not None:
            return User(customer)

        return None

    @staticmethod
    def get(user_id):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_id:
            return None
        customer = Customer.query.filter_by(id=user_id).first()

        if customer is not None:
            return User(customer)

        return None

