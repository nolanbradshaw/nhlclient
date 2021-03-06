import unittest
import nhlclient

# Constants
DIVISION_ID = 28
DIVISION_NAME = 'Scotia North'

class TestDivisions(unittest.TestCase):
        def test_all(self):
            result = nhlclient.NhlClient().divisions()
            
        def test_get(self):
            result = nhlclient.NhlClient().division(DIVISION_ID)
            
            self.assertTrue(
                result['divisions'][0]['id'] == DIVISION_ID
            )
            
            self.assertTrue(
                result['divisions'][0]['name'] == DIVISION_NAME
            )
            