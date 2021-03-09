import unittest
import nhlclient
from nhlclient import constants

# Constants
TEAM_ID = nhlclient.TEAMS['TOR']
TEAM_FULL_NAME = 'Toronto Maple Leafs'
TEAM_NAME = 'Maple Leafs'

class TestTeams(unittest.TestCase):
    
    def test_all(self):
        result = nhlclient.NhlClient().teams()
    
    def test_list(self):
        result = nhlclient.NhlClient().teams([TEAM_ID, nhlclient.TEAMS['MTL']])
    
    def test_by_id(self):
        result = nhlclient.NhlClient().team(TEAM_ID)
        
        self.assertTrue(len(result['teams']) == 1)
        self.assertTrue(result['teams'][0]['id'] == TEAM_ID)
        
        self.assertTrue(
            result['teams'][0]['name'] == TEAM_FULL_NAME
        )
        
    def test_stats(self):
        result = nhlclient.NhlClient().team_stats(TEAM_ID)

        self.assertTrue(
            result['stats'][0]['splits'][0]['team']['name'] == TEAM_FULL_NAME
        )
        self.assertTrue(
            result['stats'][0]['splits'][0]['team']['id'] == TEAM_ID
        )