import requests
import json
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.player import Player
from .models.player_stats import PlayerStats

BASE_URL = BASE_URL + '/people'

def get_by_id(id):
    try:
        url = BASE_URL + f'/{id}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['people'][0]
        
        return Player(json)
    except HTTPError:
        raise ValueError(f'No player could be found with id ({id}).')

def get_season_stats(id, season):
    try:
        url = BASE_URL + f'/{id}/stats?stats=statsSingleSeason&season={season}'
        resp = requests.get(url)        
        resp.raise_for_status()
        
        if not len(resp.json()['stats'][0]['splits']):
            raise HTTPError
        
        data = resp.json()['stats'][0]['splits'][0]['stat']         
        return PlayerStats(data)
    except HTTPError:
        raise ValueError(f'No player could be found with id ({id}).')
