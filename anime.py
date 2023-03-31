import json

import cloudscraper
import requests

scraper = cloudscraper.create_scraper()


# append data from data and data_vf to result with limit and sort by param
def append_data(data, data_vf, limit=10, sort=None, param=None):
    result = []
    for anime in data:
        result.append(anime)
        # add tag vf
        result[-1]['vf'] = False
    for anime in data_vf:
        result.append(anime)
        # add tag vf
        result[-1]['vf'] = True
    if sort:
        result = sorted(result, key=lambda k: k[param], reverse=True)
    return result[:limit]


# get data from the https://neko-sama.fr/animes-search-vostfr.json
def get_data():
    url = 'https://neko-sama.fr/animes-search-vostfr.json'
    data = scraper.get(url).json()
    return data


# get data from the https://neko-sama.fr/animes-search-vf.json
def get_data_vf():
    url = 'https://neko-sama.fr/animes-search-vf.json'
    data = scraper.get(url).json()
    return data


# get more info about the anime
def get_anime_info(url):
    trailer = ''
    html = scraper.get('https://neko-sama.fr' + url).text
    # get synopsis from the html page with class "synopsis"
    synopsis = html.split('synopsis">')[1].split('</p>')[0].split('\n')[2]
    # if trailer, get trailer from iframe
    if 'iframe' in html:
        trailer = html.split('iframe')[1].split('src="')[1].split('"')[0]
    # get banner from id head
    banner = html.split('id="head"')[1].split('src="')[1].split('"')[0]
    # get episodes from js variable episodes
    episodes = html.split('var episodes = ')[1].split(';')[0]
    # remove anti slash
    episodes = episodes.replace('\\', '')
    return {'synopsis': synopsis, 'trailer': trailer, 'banner': banner, 'episodes': json.loads(episodes)}


# search anime
def search_anime(name, data=None, data_vf=None):
    if data is None:
        data = get_data()
    if data_vf is None:
        data_vf = get_data_vf()
    result = []
    for anime in data:
        if name.lower() in anime['title'].lower():
            result.append(anime)
            # add tag vf
            result[-1]['vf'] = False
    for anime in data_vf:
        if name.lower() in anime['title'].lower():
            result.append(anime)
            # add tag vf
            result[-1]['vf'] = True
    return result


# filter anime by genre
def filter_anime(genre, data=None, data_vf=None):
    if data is None:
        data = get_data()
    if data_vf is None:
        data_vf = get_data_vf()
    result = []
    for anime in data:
        if genre in anime['genres']:
            result.append(anime)
            # add tag vf
            result[-1]['vf'] = False
    for anime in data_vf:
        if genre in anime['genres']:
            result.append(anime)
            # add tag vf
            result[-1]['vf'] = True
    return result


# get popular anime
def get_popular(data=None, data_vf=None, limit=10):
    if data is None:
        data = get_data()
    if data_vf is None:
        data_vf = get_data_vf()
    return append_data(data, data_vf, limit, True, 'popularity')


# get anime by score
def get_by_score(data=None, data_vf=None, limit=10):
    if data is None:
        data = get_data()
    if data_vf is None:
        data_vf = get_data_vf()
    return append_data(data, data_vf, limit, True, 'score')



class Anime:
    pass
