import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.schedule import Schedule

BASE_URL += '/schedule'

def get_by_date(date):
    # Get by single date
    if date is None:
        raise ValueError('Date cannot be None.')
    
    url = BASE_URL + f'?date={date}'
    resp = requests.get(url)
    data = resp.json()['dates'][0]
    
    return Schedule(data)