from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
import user_routes
import admin_routes
import customer_routes