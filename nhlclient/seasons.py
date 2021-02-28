import requests
from .constants import BASE_URL

class Seasons():
    def __init__(self):
        self.__base_url = BASE_URL + '/seasons'
    
    def all(self):
        return self.__get_season()
        
    def get(self, id):
        return self.__get_season(id)
    
    def __get_season(self, id=None):
        url = self.__base_url
        if id is not None:
            url += f'/{id}'
            
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
        