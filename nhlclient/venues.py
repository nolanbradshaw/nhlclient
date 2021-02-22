import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.venue import Venue

BASE_URL += '/venues'

def get(id = None):
    try:
        url = BASE_URL
        if id is not None:
            url += f'/{id}'

        resp = requests.get(url)
        resp.raise_for_status()
        
        data = resp.json().get('venues', None)
        if len(data) == 1:
            return Venue(data[0])
        elif len(data):
            venue_list = []
            for venue in resp.json().get('venues', []):
                venue_list.append(Venue(venue))

            return venue_list
        else:
            raise HTTPError('No venue found.')
    except HTTPError:
        raise ValueError(f'Could not find a venue with the given id ({id}).')