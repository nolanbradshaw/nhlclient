import requests
from .constants import BASE_URL

class NhlClient(object):
    def _get(self, url):
        resp = requests.get(url)
        resp.raise_for_status()
        
        return resp.json()
    
    def team(self, team_id):
        """Get a team by id.

        Args:
            team_id (int): The id of the team.
        """
        return self._get(BASE_URL + f'/teams/{team_id}')
    
    def teams(self, team_ids=[]):
        """Get a list of teams.

        Args:
            team_ids (list, optional): A list of team ids to retrieve. Defaults to [].
            
            All teams are returned if team_ids is not passed.
        """
        url = BASE_URL + f'/teams'
        if team_ids:
            url += f'?teamId=' + ','.join(str(id) for id in team_ids)
            
        return self._get(url)
    
    def team_stats(self, team_id):
        """Get a teams stats for the current season.

        Args:
            team_id (int): The id for the team.
        """
        return self._get(BASE_URL + f'/teams/{team_id}/stats')
    
    def team_roster(self, team_id):
        """Get a teams current roster.

        Args:
            team_id (int): The id for the team.
        """
        return self._get(BASE_URL + f'/teams/{team_id}?expand=team.roster')
    
    def standings(self):
        """Get the current standings.
        """
        return self._get(BASE_URL + '/standings')
    
    def schedule(self):
        """Get the schedule for the current day.
        """
        return self._get(BASE_URL + '/schedule')
    
    # schedule by date
    
    def player(self, player_id):
        """Get a players information.

        Args:
            player_id (int)): The id for the player.
        """
        return self._get(BASE_URL + f'/people/{player_id}')
    
    def player_career_stats(self, player_id):
        """Get a players career stats.

        Args:
            player_id (int): The id for the player.
        """
        return self._get(BASE_URL + f'/people/{player_id}/stats?stats=yearByYear')
    
    def player_season_stats(self, player_id, season):
        """Get a players stats by year.

        Args:
            player_id (int): The id for the player.
            season (str): The season to retrieve stats for (ex. 20162017).
        """
        return self._get(
            BASE_URL + f'/people/{player_id}/stats?stats=statsSingleSeason&season={season}'
        )
        
    def seasons(self):
        """Get a list of all seasons.
        """
        return self._get(BASE_URL + '/seasons')
    
    def season(self, season):
        """Get a season.

        Args:
            season (str): The season to retrieve (ex. 20162017).
        """
        return self._get(BASE_URL + f'/seasons/{season}')
    
    def divisions(self):
        """Get a list of all active divisions.
        """
        return self._get(BASE_URL + '/divisions')
    
    def division(self, division_id):
        """Get a division by id.

        Args:
            division_id (int): The id for the division.
        """
        return self._get(BASE_URL + f'/divisions/{division_id}')
    
    def awards(self):
        """Get a list of awards.
        """
        return self._get(BASE_URL + '/awards')
    
    def award(self, award_id):
        """Get a award.

        Args:
            award_id (int): The id for the award.
        """
        return self._get(BASE_URL + f'/awards/{award_id}')
    
    def venues(self):
        """Get a list of venues.
        """
        return self._get(BASE_URL + '/venues')
    
    def venue(self, venue_id):
        """Get a venue.

        Args:
            venue_id (int): The id for the venue.
        """
        return self._get(BASE_URL + f'/venues/{venue_id}')
    
    def draft_year(self, year):
        """Get a draft by year.

        Args:
            year (str): The year of the draft (ex. 2015).
        """
        return self._get(BASE_URL + f'/draft/{year}')