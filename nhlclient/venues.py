import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.venue import Venue

BASE_URL += '/venues'

def get():
    resp = requests.get(BASE_URL)
    
    venue_list = []
    for venue in resp.json().get('venues', []):
        venue_list.append(Venue(venue))
        
    return venue_list

def get_by_id(id):
    try:
        resp = requests.get(BASE_URL + f'/{id}')
        resp.raise_for_status()
        return Venue(resp.json().get('venues')[0])
    except HTTPError:
        raise ValueError('Could not find a venue with the given id.') 