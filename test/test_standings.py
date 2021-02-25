import unittest
from nhlclient import standings
from nhlclient.models.standings import Standings

class TestStandings(unittest.TestCase):
    def test_get(self):
        resp = standings.get()
        self.assertIsInstance(resp, list)
        self.assertIsInstance(resp[0], Standings)