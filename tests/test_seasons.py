import unittest
from nhlclient.seasons import Seasons

SEASON_ID = '20172018'

class TestSeasons(unittest.TestCase):
    def test_get(self):
        result = Seasons().all()
        
    def test_get_by_id(self):
        result = Seasons().get(SEASON_ID)
        
        self.assertTrue(
            result['seasons'][0]['seasonId'] == SEASON_ID
        )