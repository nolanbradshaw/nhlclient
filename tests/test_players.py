import unittest
from nhlclient.players import Players

# Constants
PLAYER_ID = 8471675
PLAYER_NAME = 'Sidney Crosby'
PLAYER_JERSEY_NUM = '87'
PLAYER_POSITION = 'Center'


class TestPlayers(unittest.TestCase):
    players = Players(PLAYER_ID)
    
    def test_get(self):
        result = self.players.get()
        
        self.assertTrue(len(result['people']) == 1)
        self.assertTrue(
            result['people'][0]['fullName'] == PLAYER_NAME
        )
        self.assertTrue(
            result['people'][0]['primaryNumber'] == PLAYER_JERSEY_NUM
        )
        
    def test_get_stats_by_year(self):
        result = self.players.stats_by_year('20162017')
        
        self.assertTrue(
            result['stats'][0]['type']['displayName'] == 'statsSingleSeason'
        )
        self.assertTrue(
            result['stats'][0]['splits'][0]['season'] == '20162017'
        )
        
    def test_get_career_stats_by_year(self):
        result = self.players.career_stats_by_year()