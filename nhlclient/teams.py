import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models import *

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
        
        return TeamModel(resp.json()['teams'][0])
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
    team_list = [TeamModel(team) for team in json]
    
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
        json = resp.json()['teams'][0]
    
        return [PlayerModel(player) for player in json['roster']['roster']]
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
        json = resp.json()['teams'][0]
        
        return [PlayerModel(player) for player in json['roster']['roster']]
    except HTTPError as e:
        raise ValueError(f'Could not find a team with that id ({id}) for the given season.')
    
def get_last_game(id):
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.schedule.previous'
        resp = requests.get(url)
        resp.raise_for_status()
        
        json = resp.json()['teams'][0]['previousGameSchedule']['dates'][0]
        game = json['games'][0]
        
        return GameModel(date=json['date'],
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

    
