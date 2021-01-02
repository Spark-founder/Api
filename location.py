import requests


def location():
    res = requests.get('http://ipinfo.io/')
    data = res.json()
    return data
