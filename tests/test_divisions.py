import unittest
from nhlclient.divisions import Divisions

# Constants
DIVISION_ID = 28
DIVISION_NAME = 'Scotia North'

class TestDivisions(unittest.TestCase):
        def test_all(self):
            result = Divisions().all()
            
        def test_get(self):
            result = Divisions().get(DIVISION_ID)
            
            self.assertTrue(
                result['divisions'][0]['id'] == DIVISION_ID
            )
            
            self.assertTrue(
                result['divisions'][0]['name'] == DIVISION_NAME
            )
            