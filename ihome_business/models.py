from datetime import datetime

from . import db


class BaseModel(db.Model):
    """模型基类， 为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "ih_user_profile"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, unllable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    mobile = db.Column(db.String(11), unique=False)
    real_name = db.Column(db.String(32))
    id_card = db.Column(db.String(32))
    avatar_url = db.Column(db.String(128))
    houses = db.relationship("House", backref="user")
    orders = db.relationship("Order", backref="user")


class Area(BaseModel, db.Model):
    """地区"""
    __tablename__ = "ih_area_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    houses = db.relationship("House", backref="area")


house_facility = db.Table(
    "ih_house_facility",
    db.Column("house_id", db.Integer, db.ForeignKey("ih_house_info.id"), primary_key=True),
    db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility_info.id"), primary_key=True)
)


class House(BaseModel, db.Model):
    """房子信息"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"))
    area_id = db.Column(db.Integer, db.ForeignKey("ih_area_info.id"))
    title = db.Column(db.String(64), default="")
    price = db.Column(db.Integer, default=0)
    address = db.Column(db.String(512), default="")
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 面积
    unit = db.Column(db.String(32), default="")  # 几室几厅
    capacity = db.Column(db.Integer, default=1)  # 容纳人数
    beds = db.Column(db.String(64), default="")
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)
    max_days = db.Column(db.Integer, default=0)
    order_count = db.Column(db.Integer, default=0)  # 预订完成的该房屋的订单数
    index_image_url = db.Column(db.String(256), default="")  # 房屋主图片岛路径
    facilities = db.relationship('facility', secondary=house_facility)  # 房屋的设施
    images = db.relationship("HouseImage")  # 房屋的图
    orders = db.relationship('Order', backref="house")  # 房屋的订单
