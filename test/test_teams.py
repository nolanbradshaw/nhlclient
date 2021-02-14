import unittest
from nhlclient import teams
from nhlclient.models import TeamModel, PlayerModel

class Test_Teams(unittest.TestCase):
    def test_get_by_id(self):
        response = teams.get_by_id(1)
        self.assertIsInstance(response, TeamModel)
    
    def test_get(self):
        response = teams.get()
        self.assertIsInstance(response, list)
        assert isinstance(response[0], TeamModel)
        
    def test_roster_by_id(self):
        response = teams.get_roster(1)
        self.assertIsInstance(response, list)
        assert isinstance(response[0], PlayerModel)