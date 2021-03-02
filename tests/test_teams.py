import unittest
from nhlclient.teams import Team
from nhlclient.constants import TEAMS

# Constants
TEAM_ID = TEAMS['TOR']
TEAM_FULL_NAME = 'Toronto Maple Leafs'
TEAM_NAME = 'Maple Leafs'

class TestTeams(unittest.TestCase):
    
    def test_all(self):
        result = Team().all()
    
    def test_by_id(self):
        result = Team().by_id(TEAM_ID)
        
        self.assertTrue(len(result['teams']) == 1)
        self.assertTrue(result['teams'][0]['id'] == TEAM_ID)
        
        self.assertTrue(
            result['teams'][0]['name'] == TEAM_FULL_NAME
        )
        
    def test_stats(self):
        result = Team().stats(TEAM_ID)
        
        self.assertTrue(
            result['stats'][0]['splits'][0]['team']['name'] == TEAM_FULL_NAME
        )
        self.assertTrue(
            result['stats'][0]['splits'][0]['team']['id'] == TEAM_ID
        )