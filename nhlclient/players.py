import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.player import Player


def get_by_id(id):
    try:
        url = BASE_URL + f'/people/{id}'
        resp = requests.get(url)
        resp.raise_for_status()
        json = resp.json()['people'][0]
        
        return Player(
            id=json['id'],
            full_name=json['fullName'],
            position=json['primaryPosition']['name'],
            jersey_number=json['primaryNumber'],
            birth_date=json['birthDate'],
            age=json['currentAge'],
            birth_city=json['birthCity'],
            birth_state=json['birthStateProvince'],
            birth_country=json['birthCountry'],
            nationality=json['nationality'],
            height=json['height'],
            weight=json['weight'],
            is_alternate_captain=json['alternateCaptain'],
            is_captain=json['captain'],
            is_rookie=json['rookie'],
            handedness=json['shootsCatches'],
            current_team_id=json['currentTeam']['id']
        )
    except HTTPError:
        raise ValueError(f'No player could be found with id ({id}).')

