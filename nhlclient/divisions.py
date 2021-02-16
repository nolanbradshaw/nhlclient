import requests 
from .constants import BASE_URL
from .models.division import Division


def get_divisions():
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
            abbreviation=division['abbreviation']
        ))
        
    return division_list
    