from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route("/")
def index():
    return "<h1>Homepage for Auth</h1>"