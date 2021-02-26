import unittest
from nhlclient import teams
from nhlclient.constants import TEAMS
from nhlclient.models.game import Game
from nhlclient.models.full_team import FullTeam
from nhlclient.models.simplified_player import SimplifiedPlayer

# Constants
TEAM_ID = TEAMS['TOR']
TEAM_FULL_NAME = 'Toronto Maple Leafs'
TEAM_NAME = 'Maple Leafs'

class TestTeams(unittest.TestCase):
    def test_get_by_id(self):
        response = teams.get(TEAMS['TOR'])
        
        self.assertIsInstance(response, FullTeam)
        self.assertEqual(TEAM_FULL_NAME, response.__str__())
        self.assertEqual(TEAM_NAME, response.team_name)
        self.assertEqual(TEAM_ID, response.id)
        
    def test_get_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get, 0)
    
    def test_get(self):
        response = teams.get()
        
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) == 31)
        self.assertIsInstance(response[0], FullTeam)
        
    def test_roster_by_id(self):
        response = teams.get_roster_by_id(TEAM_ID)
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertIsInstance(response[0], SimplifiedPlayer)
        
    def test_roster_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_id, 0)
    
    def test_roster_by_season(self):
        response = teams.get_roster_by_season(TEAM_ID, '20132014')
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], SimplifiedPlayer)
        self.assertTrue(response)
        
    def test_roster_by_season_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_season, TEAMS['MMR'], '20102011')
        
    def test_get_last_game(self):
        resp = teams.get_last_game(TEAM_ID)
        self.assertIsInstance(resp, Game)
        
    def test_get_last_game_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_last_game, 0)
        
    def test_get_next_game(self):
        resp = teams.get_next_game(TEAM_ID)
        self.assertIsInstance(resp, Game)
    
    def test_get_next_game_not_found(self):
        self.assertRaises(ValueError, teams.get_next_game, 0)