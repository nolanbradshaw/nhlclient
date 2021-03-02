import requests
from .constants import BASE_URL

class Players():
    def __init__(self, id):
        self.__base_url = BASE_URL + '/people'
        self.id = id
        
    def get(self):
        return self.__get_player()
    
    def stats_by_year(self, year):
        return self.__get_player_stats_by_year(year)
        
    def career_stats_by_year(self):
        return self.__get_player_career_stats_by_year()
        
    def __get_player_career_stats_by_year(self):
        url = self.__base_url + f'/{self.id}/stats?stats=yearByYear'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
        
    def __get_player_stats_by_year(self, year=None):
        url = self.__base_url + f'/{self.id}/stats?stats=statsSingleSeason&season={year}'

        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
    
    def __get_player(self):
        url = self.__base_url + f'/{self.id}'
        
        data = requests.get(url)
        data.raise_for_status()
        
        return data.json()
