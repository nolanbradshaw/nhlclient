import unittest
from nhlclient import venues
from nhlclient.models.venue import Venue

class TestVenues(unittest.TestCase):
    def test_get(self):
        resp = venues.get()

        self.assertTrue(resp)
        self.assertIsInstance(resp, list)
        self.assertIsInstance(resp[0], Venue)
        self.assertNotEqual(resp[0].name, None)
        self.assertNotEqual(resp[0].id, None)
        
    def test_get_by_id(self):
        resp = venues.get_by_id(5)

        self.assertIsInstance(resp, Venue)
        self.assertNotEqual(resp.name, None)
        self.assertNotEqual(resp.id, None)