import unittest
import nhlclient

# Constants
PLAYER_ID = 8471675
PLAYER_NAME = 'Sidney Crosby'
PLAYER_JERSEY_NUM = '87'
PLAYER_POSITION = 'Center'


class TestPlayers(unittest.TestCase):
    def test_get(self):
        result = nhlclient.NhlClient().player(PLAYER_ID)
        
        self.assertTrue(len(result['people']) == 1)
        self.assertTrue(
            result['people'][0]['fullName'] == PLAYER_NAME
        )
        self.assertTrue(
            result['people'][0]['primaryNumber'] == PLAYER_JERSEY_NUM
        )
        
    def test_get_stats_by_year(self):
        result = nhlclient.NhlClient().player_season_stats(PLAYER_ID, '20162017')
        
        self.assertTrue(
            result['stats'][0]['type']['displayName'] == 'statsSingleSeason'
        )
        self.assertTrue(
            result['stats'][0]['splits'][0]['season'] == '20162017'
        )
        
    def test_get_career_stats(self):
        result = nhlclient.NhlClient().player_career_stats(PLAYER_ID)