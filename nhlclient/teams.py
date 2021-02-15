import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models import TeamModel, DivisionModel, ConferenceModel, VenueModel, PlayerModel

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

    
