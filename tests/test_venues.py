import unittest
import nhlclient

VENUE_ID = 14
VENUE_NAME = 'Rogers Centre'

class TestVenues(unittest.TestCase):
    def test_all(self):
        result = nhlclient.NhlClient().venues()
        
    def test_get(self):
        result = nhlclient.NhlClient().venue(VENUE_ID)
        
        self.assertTrue(
            result['venues'][0]['id'] == VENUE_ID
        )
        
        self.assertTrue(
            result['venues'][0]['name'] == VENUE_NAME
        )