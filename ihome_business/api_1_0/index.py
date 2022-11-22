from . import api
from flask import current_app
from ihome_business import db, models


@api.route("/index")
def index():
    current_app.logger.error("adfs")
    return "index page"
