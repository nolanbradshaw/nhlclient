import requests
from .constants import BASE_URL
from .models.draft import Draft

BASE_URL += '/draft'

def get_draft_by_year(year):
    resp = requests.get(BASE_URL + f'/{year}')
    data = resp.json().get('drafts')[0]

    if 'rounds' not in data:
        raise ValueError('No draft exists for the given year.')
    
    draft_list = []
    for round in data.get('rounds'):
        for pick in round.get('picks'):
            draft_list.append(Draft(pick))
            
    return draft_list