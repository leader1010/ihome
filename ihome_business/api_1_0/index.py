from . import api
from flask import current_app


@api.route("/index")
def index():
    current_app.logger.error("adfs")
    return "index page"
