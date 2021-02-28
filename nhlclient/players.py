import requests
from .constants import BASE_URL

class Players():
    def __init__(self):
        self.__base_url = BASE_URL + '/people'
        
    def get(self, id):
        return self.__get_player(id)
    
    def __get_player(self, id):
        url = self.__base_url + f'/{id}'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
