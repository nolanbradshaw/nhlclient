import unittest
from nhlclient import divisions
from nhlclient.models.division import Division

# Constants
DIVISION_ID = 28
DIVISION_NAME = 'Scotia North'
DIVISION_ABBR = 'NTH'

class TestDivisions(unittest.TestCase):
        def test_get_all_divisions(self):
            response = divisions.get()
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], Division)
            self.assertTrue(response)
            
        def test_get_division_by_id(self):
            response = divisions.get(DIVISION_ID)
            self.assertEqual(DIVISION_NAME, response.__str__())
            self.assertEqual(DIVISION_ABBR, response.abbreviation)
            self.assertIsInstance(response, Division)
            
        def test_get_division_by_id_not_found(self):
            self.assertRaises(ValueError, divisions.get, 0)
            