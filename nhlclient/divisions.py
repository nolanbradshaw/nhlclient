import requests 
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.division import Division


def get():
    """
        Get a list of divisions.

    Returns:
        List: A list of Division objects.
    """
    url = BASE_URL + f'/divisions'
    resp = requests.get(url)
    json = resp.json()['divisions']
    
    division_list = []
    for division in json:
        division_list.append(Division(
            id=division['id'],
            name=division['name'],
            abbreviation=division['abbreviation'],
            is_active=division['active']
        ))
        
    return division_list

def get_by_id(id):
    """
        Get a division by id.

    Args:
        id (int): The divisions id.

    Raises:
        ValueError: A division could not be found for the given id.

    Returns:
        Division: A Division object.
    """
    try:
        url = BASE_URL + f'/divisions/{id}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()
        
        # API returns an empty object with a 200 if not found.
        if not len(json['divisions']):
            raise HTTPError
        
        division = json['divisions'][0]
        return Division(
            id=division['id'],
            name=division['name'],
            abbreviation=division['abbreviation'],
            is_active=division['active']
        )
    except HTTPError:
        raise ValueError(f'Could not find a division with id ({id}).')
    