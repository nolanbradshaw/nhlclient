import requests
from .constants import BASE_URL

class Venues():
    def __init__(self):
        self.__base_url = BASE_URL + '/venues'
        
    def all(self):
        return self.__get_venue()    
    
    def get(self, id):
        return self.__get_venue(id)
    
    def __get_venue(self, id=None):
        url = self.__base_url
        if id is not None:
            url += f'/{id}'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()