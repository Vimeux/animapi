

from flask import Flask, jsonify, request

from anime import get_data, get_data_vf, get_anime_info

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


if __name__ == '__main__':
    app.run()
