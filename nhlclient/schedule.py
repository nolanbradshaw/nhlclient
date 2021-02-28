import requests
from .constants import BASE_URL

class Schedule():
    def __init__(self):
        self.__base_url = BASE_URL + '/schedule'
        
    def by_date(self, date):
        return self.__get_by_date(date)
        
    def __get_by_date(self, date):
        url = self.__base_url + f'?date={date}'
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()