# coding: utf-8
import redis


class Config(object):
    """工程配置信息"""
    SECRET_KEY = "1234SDFJKH"

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session用到的配置信息
    SESSION_TYPE = "redis"  # 指明保存到session
    SESSION_USE_SIGNER = True  # 对cookie中的session_id设置隐藏处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位：秒


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    ...


config_dict = {
    "dev": DevConfig,
    "prod": ProductionConfig,
}
