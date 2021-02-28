import requests
from .constants import BASE_URL

class Awards():
    def __init__(self):
        self.__base_url = BASE_URL + '/awards'
        
    def all(self):
        return self.__get_award()
    
    def by_id(self, id):
        return self.__get_award(id)
        
    def __get_award(self, id=None):
        url = self.__base_url
        if id is not None:
            url += f'/{id}'
            
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()