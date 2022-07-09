import requests


def clever_hero(*hero_names):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    intelligence = 0
    name = ''
    for hero in response:
        if hero['name'] in hero_names and hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            name = hero['name']
    return f'{name = }, {intelligence = }'

if __name__ == '__main__':
    print(clever_hero('Hulk', 'Thanos', 'Captain America'))
