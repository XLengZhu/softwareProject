from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 配置CORS，允许所有来源
CORS(app)

def create_app():
    from app import models, views
    return app

app = create_app()

@app.before_request
def handle_options_requests():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    else:
        return None

def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
    return response

# 创建数据库表
with app.app_context():
    db.create_all()
