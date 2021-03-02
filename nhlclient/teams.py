import requests
from .constants import BASE_URL

class Team:
    def __init__(self):
        self.__base_url = BASE_URL + '/teams'
    
    def all(self):
        return self.__get_team()
    
    def by_id(self, id):
        return self.__get_team(id)
    
    def stats(self, id):
        return self.__get_stats(id)
    
    def __get_stats(self, id):
        url = self.__base_url + f'/{id}/stats'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()

    def __get_team(self, id = None):
        url = self.__base_url
        if id is not None:
            url += f'/{id}'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
        

    
