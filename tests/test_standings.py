import unittest
import nhlclient

class TestStandings(unittest.TestCase):
    def test_all(self):
        result = nhlclient.NhlClient().standings()