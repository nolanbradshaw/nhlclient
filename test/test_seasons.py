import unittest
from nhlclient import seasons
from nhlclient.models.season import Season

class TestSeasons(unittest.TestCase):
    def test_get(self):
        resp = seasons.get()
        self.assertIsInstance(resp, list)
        self.assertIsInstance(resp[0], Season)
        
    def test_get_by_id(self):
        resp = seasons.get('20172018')
        self.assertIsInstance(resp, Season)