import requests
from .constants import BASE_URL
from .models import TeamModel, DivisionModel, ConferenceModel, VenueModel, PlayerModel

def get_by_id(id):
    """
    Get a teams information by its id.

    Args:
        id (int): The id for the team.

    Returns:
        [TeamModel]: The TeamModel object.
    """
    
    url = BASE_URL + f'/teams/{id}'
    response = requests.get(url)
    json = response.json()['teams'][0]
    return TeamModel(json)

def get():
    """
    Get information for all teams.

    Returns:
        [List of TeamModel]: A list of TeamModel objects.
    """
    response = requests.get(BASE_URL + '/teams')
    json = response.json()['teams']
    team_list = [TeamModel(team) for team in json]
    
    return team_list

def get_roster_by_id(id):
    """
    Get a teams roster by id.

    Args:
        id (int): The id for the team.

    Returns:
        [List of PlayerModel]: A list of PlayerModel objects.
    """
    
    url = BASE_URL + f'/teams/{id}?expand=team.roster'
    response = requests.get(url)
    json = response.json()['teams'][0]
    
    return [PlayerModel(player) for player in json['roster']['roster']]

def get_roster_by_season(id, season):
    """
    Get a teams roster for a specific season.

    Args:
        id (int): The id for the team.
        season (str): The season to retrieve the roster (Ex. 20132014).

    Returns:
        [List of PlayerModel]: A list of PlayerModel objects.
    """
    
    url = BASE_URL + f'/teams/{id}?expand=team.roster&season={season}'
    response = requests.get(url)
    json = response.json()['teams'][0]
    return [PlayerModel(player) for player in json['roster']['roster']]

    
