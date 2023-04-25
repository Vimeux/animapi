from flask import Blueprint

anime_blueprint = Blueprint('anime', __name__)

from app.routes.anime import *