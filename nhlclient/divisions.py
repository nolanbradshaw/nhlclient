import requests 
from .constants import BASE_URL

class Divisions():
    def __init__(self):
        self.__base_url = BASE_URL + '/divisions'
        
    def all(self):
        return self.__get_division()
    
    def get(self, id):
        return self.__get_division(id)
    
    def __get_division(self, id=None):
        url = self.__base_url
        if id is not None:
            url += f'/{id}'
            
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
        
    