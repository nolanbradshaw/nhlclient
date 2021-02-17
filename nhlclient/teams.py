import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.game import Game
from .models.roster import Roster
from .models.team import Team

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
        data = resp.json()['teams'][0]
        return Team(data)
    except HTTPError:
        raise ValueError(f'Could not find a team with that id ({id}).')

def get():
    """
    Get information for all teams.

    Returns:
        List: A list of TeamModel objects.
    """
    resp = requests.get(BASE_URL + '/teams')
    json = resp.json()['teams']
    team_list = []
    for team in json:
        team_list.append(Team(team))
    
    return team_list

def get_roster_by_id(id):
    """
    Get a teams roster by id.

    Args:
        id (int): The id for the team.

    Raises:
        ValueError: Could not find a team with the given id.

    Returns:
        List: A list of PlayerModel objects.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.roster'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['teams'][0]['roster']['roster']

        player_list = []
        for player in json:
            player_list.append(Roster(player))
            
        return player_list
    except HTTPError:
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
        List: A list of PlayerModel objects.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.roster&season={season}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['teams'][0]['roster']['roster']
        
        player_list = []
        for player in json:   
            player_list.append(Roster(player))
        
        return player_list
    except HTTPError:
        raise ValueError(f'Could not find a team with that id ({id}) for the given season.')
    
def get_last_game(id):
    """
    Get a teams last played game.

    Args:
        id (int): The id for the team.

    Raises:
        ValueError: Could not find a team with the given id.
        
    Returns:
        Game: A Game object.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.schedule.previous'
        resp = requests.get(url)
        resp.raise_for_status()
        
        json = resp.json()['teams'][0]['previousGameSchedule']['dates'][0]
        data = json['games'][0]
        
        return Game(data)
    except HTTPError:
        raise ValueError(f'Could not find a team with that id ({id}).')
    
def get_next_game(id):
    """
    Get a teams next game.

    Args:
        id (int): The id for the team.

    Raises:
        ValueError: Could not find a team with the given id.

    Returns:
        Game: A Game object.
    """
    try:
        url = BASE_URL + f'/teams/{id}?expand=team.schedule.next'
        resp = requests.get(url)
        resp.raise_for_status()
        
        json = resp.json()['teams'][0]['nextGameSchedule']['dates'][0]
        data = json['games'][0]
        
        return Game(data)
    except HTTPError:
        raise ValueError(f'Could not find a team with that id ({id}).')
        

    
