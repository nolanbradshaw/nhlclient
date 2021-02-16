import requests
from .constants import BASE_URL
from .models.game import Game
from .models.player import Player
from .models.team import Team
from requests.exceptions import HTTPError

def get_by_id(id):
    """
    Get a teams information by its id.

    Args:
        id (int): The id for the team.
    
    Raises:
        ValueError: Could not find a team with the given id.

    Returns:
        TeamModel: The TeamModel object.
    """
    try:
        url = BASE_URL + f'/teams/{id}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['teams'][0]
        return Team(
            id=json['id'],
            name=json['name'],
            team_name=json['teamName'],
            official_site_url=json['officialSiteUrl']
        )
    except HTTPError as e:
        raise ValueError(f'Could not find a team with that id ({id}).')

def get():
    """
    Get information for all teams.

    Returns:
        List of TeamModel: A list of TeamModel objects.
    """
    resp = requests.get(BASE_URL + '/teams')
    json = resp.json()['teams']
    team_list = []
    for team in json:
        team_list.append(Team(
            id=team['id'],
            name=team['name'],
            team_name=team['teamName'],
            official_site_url=team['officialSiteUrl']
        ))
    
    return team_list

def get_roster_by_id(id):
    """
    Get a teams roster by id.

    Args:
        id (int): The id for the team.

    Raises:
        ValueError: Could not find a team with the given id.

    Returns:
        List of PlayerModel: A list of PlayerModel objects.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.roster'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['teams'][0]['roster']['roster']

        player_list = []
        for player in json:
            jersey_num = 0
            if 'jerseyNumber' in player:
                jersey_num = player['jerseyNumber']
                
            player_list.append(Player(
                id=player['person']['id'],
                name=player['person']['fullName'],
                position=player['position']['name'],
                jersey_number=jersey_num
            ))
            
        return player_list
    except HTTPError as e:
        raise ValueError(f'Could not find a team with that id ({id}).')

def get_roster_by_season(id, season):
    """
    Get a teams roster for a specific season.

    Args:
        id (int): The id for the team.
        season (str): The season to retrieve the roster (Ex. 20132014).

    Raises:
        ValueError: Could not find team by id for the given season.

    Returns:
        List of PlayerModel: A list of PlayerModel objects.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.roster&season={season}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['teams'][0]['roster']['roster']
        
        player_list = []
        for player in json:
            jersey_num = 0
            if 'jerseyNumber' in player:
                jersey_num = player['jerseyNumber']
                
            player_list.append(Player(
                id=player['person']['id'],
                name=player['person']['fullName'],
                position=player['position']['name'],
                jersey_number=jersey_num
            ))
        
        return player_list
    except HTTPError as e:
        raise ValueError(f'Could not find a team with that id ({id}) for the given season.')
    
def get_last_game(id):
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.schedule.previous'
        resp = requests.get(url)
        resp.raise_for_status()
        
        json = resp.json()['teams'][0]['previousGameSchedule']['dates'][0]
        game = json['games'][0]
        
        return Game(date=json['date'],
                         game_id=game['gamePk'],
                         season=game['season'],
                         detailed_status=game['status']['detailedState'],
                         away_team_id=game['teams']['away']['team']['id'],
                         away_team_name=game['teams']['away']['team']['name'],
                         away_team_score=game['teams']['away']['score'],
                         home_team_id=game['teams']['home']['team']['id'],
                         home_team_name=game['teams']['home']['team']['name'],
                         home_team_score=game['teams']['home']['score'])
    except HTTPError as e:
        raise ValueError(f'Could not find a team with that id ({id}).')

    
