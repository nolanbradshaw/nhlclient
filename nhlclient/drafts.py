import requests
from .constants import BASE_URL

class Drafts():
    def __init__(self):
        self.__base_url = BASE_URL + '/draft'
        
    def by_year(self, year):
        return self.__get_by_year(year)
        
    def __get_by_year(self, year):
        data = requests.get(self.__base_url + f'/{year}')
        data.raise_for_status()
        
        return data.json()