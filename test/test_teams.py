import unittest
from nhlclient import teams
from nhlclient.constants import TEAMS
from nhlclient.models.game import Game
from nhlclient.models.player import Player
from nhlclient.models.team import Team

class TestTeams(unittest.TestCase):
    def test_get_by_id(self):
        response = teams.get_by_id(TEAMS['TOR'])
        self.assertIsInstance(response, Team)
        
    def test_get_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_by_id, 0)
    
    def test_get(self):
        response = teams.get()
        self.assertIsInstance(response, list)
        assert isinstance(response[0], Team)
        
    def test_roster_by_id(self):
        response = teams.get_roster_by_id(TEAMS['TBL'])
        self.assertIsInstance(response, list)
        assert isinstance(response[0], Player)
        
    def test_roster_by_id_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_id, 0)
    
    def test_roster_by_season(self):
        response = teams.get_roster_by_season(TEAMS['TOR'], '20132014')
        self.assertIsInstance(response, list)
        assert isinstance(response[0], Player)
        
    def test_roster_by_season_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_roster_by_season, TEAMS['MMR'], '20102011')
        
    def test_get_last_game(self):
        response = teams.get_last_game(TEAMS['EDM'])
        self.assertIsInstance(response, Game)
        
    def test_get_last_game_not_found(self):
        """
            Should raise a ValueError as no team with id 0 exists.
        """
        self.assertRaises(ValueError, teams.get_last_game, 0)
        
    def test_get_next_game(self):
        response = teams.get_next_game(TEAMS['VAN'])
        self.assertIsInstance(response, Game)
    
    def test_get_next_game_not_found(self):
        self.assertRaises(ValueError, teams.get_next_game, 0)