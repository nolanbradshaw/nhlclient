import requests
from .models.standings import Standings
from .constants import BASE_URL
from requests.exceptions import HTTPError

BASE_URL += '/standings'

def get():
    url = BASE_URL
    
    resp = requests.get(url)
    data = resp.json().get('records')
    
    standings_list = []
    for record in data:
        for team in record.get('teamRecords', []):
            standings_list.append(Standings(team))
            
    return standings_list
    