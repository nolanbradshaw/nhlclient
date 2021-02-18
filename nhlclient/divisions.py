import requests 
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.division import Division


def get(id = None):
    """
        Get division by id (all divisions if no id is provided).

    Returns:
        Division: A Division object/list.
    """
    try:
        url = BASE_URL + f'/divisions'
        if id is not None:
            url += f'/{id}'

        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['divisions']

        if len(json) == 1:
            return Division(json[0])
        elif len(json):
            division_list = []
            for division in json:
                division_list.append(Division(division))

            return division_list
        else:
            raise HTTPError('No division found.') 
    except HTTPError:
        raise ValueError(f'No division could be found for the given id ({id})')
        
    