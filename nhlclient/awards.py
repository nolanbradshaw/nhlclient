import requests
from requests.exceptions import HTTPError
from .models.award import Award
from .constants import BASE_URL

BASE_URL += '/awards'

def get():
    resp = requests.get(BASE_URL)
    data = resp.json().get('awards', [])
    
    award_list = []
    for award in data:
        award_list.append(Award(award))
    
    return award_list

def get_by_id(id):
    try:
        resp = requests.get(BASE_URL + f'/{id}')
        resp.raise_for_status()
        data = resp.json().get('awards', [{}])[0]
        return Award(data)
    except HTTPError:
        return ValueError(f'No award was found for the given id ({id}).')