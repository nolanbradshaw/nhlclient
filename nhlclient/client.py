import requests
from .constants import BASE_URL

class NhlClient(object):
    def _get(self, url):
        resp = requests.get(url)
        resp.raise_for_status()
        
        return resp.json()
    
    def team(self, team_id):
        return self._get(BASE_URL + f'/teams/{team_id}')
    
    def teams(self, team_ids=[]):
        url = BASE_URL + f'/teams'
        if team_ids:
            url += f'?teamId=' + ','.join(str(id) for id in team_ids)
            
        return self._get(url)
    
    def team_stats(self, team_id):
        return self._get(BASE_URL + f'/teams/{team_id}/stats')
    
    def standings(self):
        return self._get(BASE_URL + '/standings')
    
    def schedule(self):
        return self._get(BASE_URL + '/schedule')
    
    # schedule by date
    
    def player(self, player_id):
        return self._get(BASE_URL + f'/people/{player_id}')
    
    def player_career_stats(self, player_id):
        return self._get(BASE_URL + f'/people/{player_id}/stats?stats=yearByYear')
    
    def player_year_stats(self, player_id, year):
        return self._get(
            BASE_URL + f'/people/{player_id}/stats?stats=statsSingleSeason&season={year}'
        )
        
    def seasons(self):
        return self._get(BASE_URL + '/seasons')
    
    def season(self, season):
        return self._get(BASE_URL + f'/seasons/{season}')
    
    def divisions(self):
        return self._get(BASE_URL + '/divisions')
    
    def division(self, division_id):
        return self._get(BASE_URL + f'/divisions/{division_id}')
    
    def awards(self):
        return self._get(BASE_URL + '/awards')
    
    def award(self, award_id):
        return self._get(BASE_URL + f'/awards/{award_id}')
    
    def venues(self):
        return self._get(BASE_URL + '/venues')
    
    def venue(self, venue_id):
        return self._get(BASE_URL + f'/venues/{venue_id}')
    
    def draft_year(self, year):
        return self._get(BASE_URL + f'/draft/{year}')