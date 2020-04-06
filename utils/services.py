import json
import urllib3
import private
urllib3.disable_warnings()

#TODO Put all the base and the token in a configuration file
http_client = urllib3.PoolManager()
def dragon_base():
    return "http://ddragon.leagueoflegends.com"
def API_base():
    return "https://euw1.api.riotgames.com"
def statics_base():
    return "http://static.developer.riotgames.com"
def token():
    return private.token()

def fetch_url(url, method = 'GET'):
    print(f"{url}")
    return http_client.request(method, f"{url}")

def fetch_statics(url):
    return fetch_url(f"{statics_base()}{url}")
def fetch_riot_API(url):
    return fetch_url(f"{API_base()}{url}?api_key={token()}")
def fetch_dragons(url):
    return fetch_url(f"{dragon_base()}{url}")

def url_dragons(url):
    return f"{dragon_base()}{url}"
