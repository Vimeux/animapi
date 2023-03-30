import json

import cloudscraper
import requests

scraper = cloudscraper.create_scraper()


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
    # print(episodes)


    # episodeList = []
    # for row in episodes:
    #     episode = {
    #         'time': row.select_one('div[itemprop="duration"]').text.strip(),
    #         'episode': row.select_one('div.episode').text.strip(),
    #         'num': row.select_one('div.num').text.strip(),
    #         'title': row.select_one('div.title').text.strip(),
    #         'url': row.select_one('div.title a').get('href'),
    #         'url_image': row.select_one('div.img img').get('src')
    #     }
    #     episodeList.append(episode)
    return {'synopsis': synopsis, 'trailer': trailer, 'banner': banner, 'episodes': json.loads(episodes)}



class Anime:
    pass
