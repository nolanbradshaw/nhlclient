import unittest
from nhlclient import divisions
from nhlclient.models.division import Division

class TestDivisions(unittest.TestCase):
        def test_get_divisions(self):
            response = divisions.get()
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], Division)
            
        def test_get_division_by_id(self):
            response = divisions.get_by_id(1)
            self.assertIsInstance(response, Division)
            
        def test_get_division_by_id_not_found(self):
            self.assertRaises(ValueError, divisions.get_by_id, 0)
            