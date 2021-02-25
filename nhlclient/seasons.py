import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.season import Season

BASE_URL += '/seasons'

def get(id = None):
    try:
        url = BASE_URL
        if id is not None:
            url += f'/{id}'
        
        resp = requests.get(url)
        resp.raise_for_status()
        
        data = resp.json().get('seasons')
        if len(data) == 1:
            return Season(data[0])
        elif len(data):
            season_list = []
            for season in data:
                season_list.append(Season(season))
    
            return season_list
        else:
            raise HTTPError('No season found.')
    except HTTPError:
        raise ValueError('No season found.')
        