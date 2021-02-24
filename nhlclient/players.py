import requests
import json
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.full_player import FullPlayer

BASE_URL = BASE_URL + '/people'
EXPAND_QUERY = '?person.currentTeam'

def get_by_id(id):
    try:
        url = BASE_URL + f'/{id}{EXPAND_QUERY}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['people'][0]
        
        return FullPlayer(json)
    except HTTPError:
        raise ValueError(f'No player could be found with id ({id}).')
