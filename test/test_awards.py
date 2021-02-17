import unittest
from nhlclient import awards
from nhlclient.models.award import Award

class TestAwards(unittest.TestCase):
    def test_get(self):
        resp = awards.get()
        self.assertIsInstance(resp, list)
        self.assertIsInstance(resp[0], Award)