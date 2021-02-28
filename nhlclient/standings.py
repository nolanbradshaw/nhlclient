import requests
from .constants import BASE_URL

class Standings():
    def __init__(self):
        self.__base_url = BASE_URL + '/standings'
        
    def all(self):
        return self.__get_standings()
        
    def __get_standings(self):
        data = requests.get(self.__base_url)
        data.raise_for_status()
        
        return data.json()
    