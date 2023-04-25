from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from app.routes import anime_blueprint
from app.models import AnimeModel
from app.config import database

anime_collection = database.db.anime

# get all anime
@anime_blueprint.route('/anime', methods=['GET'])
def get_anime():
    anime = list(anime_collection.find())
    for anime in anime:
        anime['_id'] = str(anime['_id'])
    return jsonify(anime)

# get one anime
# post one anime
# update one anime
# delete one anime

# get all episodes of one anime
# get one episode of one anime
# post one episode of one anime
# update one episode of one anime
# delete one episode of one anime

# check data of later anime