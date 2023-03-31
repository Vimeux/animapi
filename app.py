

from flask import Flask, jsonify, request

from anime import get_data, get_data_vf, get_anime_info, search_anime, filter_anime, get_popular, get_by_score

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/anime')
def anime():
    data = get_data()
    return jsonify(data)


@app.route('/animevf')
def animeVF():
    data = get_data_vf()
    return jsonify(data)


@app.route('/anime/data')
def animeinfo():
    # get url from the body json
    url = request.json['url']
    data = get_anime_info(url)
    return jsonify(data)


@app.route('/anime/search')
def search():
    # get name from the body json
    name = request.json['name']
    data = search_anime(name)
    return jsonify(data)


@app.route('/anime/filter')
def filter():
    # get genre from the body json
    genre = request.json['genre']
    data = filter_anime(genre)
    return jsonify(data)


@app.route('/anime/popular')
def popular():
    limit = request.json['limit']
    data = get_popular(limit=limit)
    return jsonify(data)


@app.route('/anime/score')
def score():
    limit = request.json['limit']
    data = get_by_score(limit=limit)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
