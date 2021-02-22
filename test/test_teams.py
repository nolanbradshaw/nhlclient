import unittest
from nhlclient import teams
from nhlclient.constants import TEAMS
from nhlclient.models.game import Game
from nhlclient.models.player import Player
from nhlclient.models.team import Team
from nhlclient.models.roster import Roster

# Constants
TEAM_ID = TEAMS['TOR']
TEAM_FULL_NAME = 'Toronto Maple Leafs'
TEAM_NAME = 'Maple Leafs'

class TestTeams(unittest.TestCase):
    def test_get_by_id(self):
        response = teams.get(TEAMS['TOR'])
        
        # Check that the TeamRecord variables were set properly
        [self.assertNotEqual(value, None) for name, value in vars(response.record).items()]
        self.assertIsInstance(response, Team)
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
        
        # Check that the TeamRecord variables were set properly
        [self.assertNotEqual(value, None) for name, value in vars(response[0].record).items()]
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) == 31)
        self.assertIsInstance(response[0], Team)
        
    def test_roster_by_id(self):
        response = teams.get_roster_by_id(TEAM_ID)
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertIsInstance(response[0], Roster)
        
    def test_roster_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_id, 0)
    
    def test_roster_by_season(self):
        response = teams.get_roster_by_season(TEAM_ID, '20132014')
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Roster)
        self.assertTrue(response)
        
    def test_roster_by_season_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_season, TEAMS['MMR'], '20102011')
        
    def test_get_last_game(self):
        response = teams.get_last_game(TEAM_ID)
        self.assertIsInstance(response, Game)
        
    def test_get_last_game_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_last_game, 0)
        
    def test_get_next_game(self):
        response = teams.get_next_game(TEAM_ID)
        self.assertIsInstance(response, Game)
    
    def test_get_next_game_not_found(self):
        self.assertRaises(ValueError, teams.get_next_game, 0)