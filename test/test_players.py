import unittest
from nhlclient import players
from nhlclient.models.player_stats import PlayerStats
from nhlclient.models.player import Player

# Constants
SEASON = '20162017'
PLAYER_ID = 8471675
PLAYER_NAME = 'Sidney Crosby'
PLAYER_JERSEY_NUM = '87'
PLAYER_POSITION = 'Center'
PLAYER_NATIONALITY = 'CAN'
PLAYER_SHOTS = 255
PLAYER_GOALS = 44
PLAYER_ASSISTS = 45
TEAM_ID = 5
TEAM_NAME = 'Pittsburgh Penguins'


class TestPlayers(unittest.TestCase):
    def test_get_players_by_id(self):
        response = players.get_by_id(PLAYER_ID)

        self.assertEqual(response.team.id, TEAM_ID)
        self.assertEqual(response.team.full_name, TEAM_NAME)
        self.assertIsInstance(response, Player)
        self.assertEqual(PLAYER_NAME, response.__str__())
        self.assertEqual(PLAYER_JERSEY_NUM, response.jersey_number)
        self.assertEqual(PLAYER_NATIONALITY, response.nationality)
            
    def test_get_players_by_id_not_found(self):
        self.assertRaises(ValueError, players.get_by_id, -1)
        
    def test_get_player_season_stats(self):
        response = players.get_season_stats(PLAYER_ID, SEASON)
        
        self.assertEqual(PLAYER_SHOTS, response.shots)
        self.assertEqual(PLAYER_GOALS, response.goals)
        self.assertEqual(PLAYER_ASSISTS, response.assists)
        self.assertIsInstance(response, PlayerStats)
        
    def test_get_player_season_stats_not_found(self):
        self.assertRaises(ValueError, players.get_season_stats, 0, '20202021')