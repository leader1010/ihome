import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config_dict
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

db = SQLAlchemy()
redis_store = None
# 为flask 应用补充csrf防护机制
csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)
    cfg = config_dict[config_name]
    app.config.from_object(cfg)
    # 初始化mysql数据库
    db.init_app(app)
    # redis
    global redis_store
    redis_store = redis.StrictRedis(host=cfg.REDIS_HOST, port=cfg.REDIS_PORT)
    csrf.init_app(app)
    Session(app)
    import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1_0")
    return app
