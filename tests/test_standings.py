import unittest
from nhlclient.standings import Standings

class TestStandings(unittest.TestCase):
    def test_all(self):
        result = Standings().all()