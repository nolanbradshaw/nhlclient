import unittest
from pprint import pprint
from nhlclient import teams
from nhlclient.models import *

class Test_Teams(unittest.TestCase):
    def test_get_by_id(self):
        response = teams.get_by_id(1)
        self.assertIsInstance(response, TeamModel)
        
    def test_get_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_by_id, 0)
    
    def test_get(self):
        response = teams.get()
        self.assertIsInstance(response, list)
        assert isinstance(response[0], TeamModel)
        
    def test_roster_by_id(self):
        response = teams.get_roster_by_id(1)
        self.assertIsInstance(response, list)
        assert isinstance(response[0], PlayerModel)
        
    def test_roster_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_id, 0)
    
    def test_roster_by_season(self):
        response = teams.get_roster_by_season(1, '20132014')
        self.assertIsInstance(response, list)
        assert isinstance(response[0], PlayerModel)
        
    def test_roster_by_season_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_season, 0, '20102011')
        
    def test_get_last_game(self):
        response = teams.get_last_game(1)
        self.assertIsInstance(response, GameModel)
        
    def test_get_last_game_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_last_game, 0)