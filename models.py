import os
from app import db
import jwt
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    # admin_product_id = db.Column(db.Integer, db.ForeignKey('admin_product.id'))
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.now)
    role = db.Column(db.String(20))
    # admin_product = relationship("Admin_product", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.id}>"
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_auth_token(self):
        expiration_time = datetime.now() + timedelta(days=10)
        payload = {
            'id': self.id,
            'exp': expiration_time
        }
        token = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')
        return token
    @staticmethod
    def verify_auth_token(token):
        if not token:
            return None
        try:
            payload = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            user = User.query.get(payload['id'])
            return user
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
            return None
        except jwt.DecodeError:
            print("Token is invalid.")
            return None
        

class Admin_product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    # role = db.Column(db.String(20))
    description = db.Column(db.String(500))
    price = db.Column(db.Integer)
    stock = db.Column(db.String(300))
    category = db.Column(db.String(300))
    # user = relationship("User", back_populates="admin_product")
    
    def __repr__(self):
        return f"<Product {self.id}"
    def format(self):
        return{
            'id': self.id,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'category': self.category
        }
        
    
# user should be able to view search product
class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.Integer)
    # stock = db.Column(db.String(300))
    category = db.Column(db.String(300))
    
    def __init__(self, product_name,description, price,  category):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.category = category
    
    # def format(self):
    #     return{
    #         'id': self.id,
    #         'product_name': self.product_name,
    #         'description': self.description,
    #         'price': self.price,
    #         'category': self.category
    #     }
        
    
    
    