import requests
from requests.exceptions import HTTPError
from .models.award import Award
from .constants import BASE_URL

BASE_URL += '/awards'

def get(id = None):
    try:
        url = BASE_URL 
        if id is not None:
            url += f'/{id}'

        resp = requests.get(url)
        data = resp.json().get('awards', [{}])

        if len(data) == 1:
            return Award(data[0])
        elif len(data):
            award_list = []
            for award in data:
                award_list.append(Award(award))
            return award_list
        else:
            raise HTTPError()
    except HTTPError:
        raise ValueError('No award could be found')