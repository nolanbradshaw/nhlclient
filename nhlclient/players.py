import requests
from requests.exceptions import HTTPError
from .constants import BASE_URL
from .models.player import Player
from .models.goalie_stats import GoalieStats
from .models.player_stats import PlayerStats

BASE_URL = BASE_URL + '/people'

def get_by_id(id):
    try:
        url = BASE_URL + f'/{id}'
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
    
def get_goalie_season_stats(id, season):
    try:
        url = BASE_URL + f'/{id}/stats?stats=statsSingleSeason&season={season}'
        resp = requests.get(url)        
        resp.raise_for_status()
        
        if not len(resp.json()['stats'][0]['splits']):
            raise HTTPError
    
        json = resp.json()['stats'][0]['splits'][0]['stat']
        
        if 'saves' not in json:
            raise TypeError('The given id was not for a goaltender (Condersider using get_player_season_stats() instead).')
        
        return GoalieStats(
            time_on_ice=json['timeOnIce'],
            shutouts=json['shutouts'],
            wins=json['wins'],
            losses=json['losses'],
            saves=json['saves'],
            power_play_saves=json['powerPlaySaves'],
            short_handed_saves=json['shortHandedSaves'],
            even_strength_saves=json['evenSaves'],
            short_handed_shots=json['shortHandedShots'],
            even_strength_shots=json['evenShots'],
            power_play_shots=json['powerPlayShots'],
            save_pct=json['savePercentage'],
            goals_against_avg=json['goalAgainstAverage'],
            games=json['games'],
            games_started=json['gamesStarted'],
            shots_against=json['shotsAgainst'],
            goals_against=json['goalsAgainst'],
            power_play_save_pct=json['powerPlaySavePercentage'],
            short_handed_save_pct=json['shortHandedSavePercentage'],
            even_strength_save_pct=json['evenStrengthSavePercentage']
        )
    except HTTPError:
        raise ValueError(f'No goalie could be found with id ({id}).')

def get_player_season_stats(id, season):
    try:
        url = BASE_URL + f'/{id}/stats?stats=statsSingleSeason&season={season}'
        resp = requests.get(url)        
        resp.raise_for_status()
        
        if not len(resp.json()['stats'][0]['splits']):
            raise HTTPError
    
        json = resp.json()['stats'][0]['splits'][0]['stat']
        
        if 'goals' not in json:
            raise TypeError('The given id was not for a player (Consider using get_player_season_stats() instead).')
        
        return PlayerStats(
            time_on_ice=json['timeOnIce'],
            assists=json['assists'],
            goals=json['goals'],
            penalty_mins=json['pim'],
            shots=json['shots'],
            games=json['games'],
            hits=json['hits'],
            power_play_goals=json['powerPlayGoals'],
            power_play_points=json['powerPlayPoints'],
            power_play_time_on_ice=json['powerPlayTimeOnIce'],
            even_time_on_ice=json['evenTimeOnIce'],
            faceoff_pct=json['faceOffPct'],
            shot_pct=json['shotPct'],
            game_winning_goals=json['gameWinningGoals'],
            overtime_goals=json['overTimeGoals'],
            shorthanded_goals=json['shortHandedGoals'],
            shorthanded_points=json['shortHandedPoints'],
            shorthanded_time_on_ice=json['shortHandedTimeOnIce'],
            blocked_shots=json['blocked'],
            plus_minus=json['plusMinus'],
            points=json['points'],
            shifts=json['shifts'],
            time_on_ice_per_game=json['timeOnIcePerGame'],
            even_time_on_ice_per_game=json['evenTimeOnIcePerGame'],
            shorthanded_time_on_ice_per_game=json['shortHandedTimeOnIcePerGame'],
            power_play_time_on_ice_per_game=json['powerPlayTimeOnIcePerGame']
        )
    except HTTPError:
        raise ValueError(f'No player could be found with id ({id}).')
