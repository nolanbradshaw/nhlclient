import unittest
import nhlclient

SEASON_ID = '20172018'

class TestSeasons(unittest.TestCase):
    def test_seasons(self):
        result = nhlclient.NhlClient().seasons()
        
    def test_season_by_id(self):
        result = nhlclient.NhlClient().season(SEASON_ID)
        self.assertTrue(result['seasons'][0]['seasonId'] == SEASON_ID)