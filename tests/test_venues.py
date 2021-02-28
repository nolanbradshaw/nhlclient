import unittest
from nhlclient.venues import Venues

VENUE_ID = 14
VENUE_NAME = 'Rogers Centre'

class TestVenues(unittest.TestCase):
    def test_all(self):
        result = Venues().all()
        
    def test_get(self):
        result = Venues().get(VENUE_ID)
        
        self.assertTrue(
            result['venues'][0]['id'] == VENUE_ID
        )
        
        self.assertTrue(
            result['venues'][0]['name'] == VENUE_NAME
        )