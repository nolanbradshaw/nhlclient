import unittest
from nhlclient import awards
from nhlclient.models.award import Award

# Constants
AWARD_ID = 2
AWARD_NAME = 'Jack Adams Award'
AWARD_SHORT_NAME = 'adams'

class TestAwards(unittest.TestCase):
    def test_get(self):
        resp = awards.get()
        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertIsInstance(resp[0], Award)
        
    def test_get_by_id(self):
        resp = awards.get_by_id(2)
        self.assertIsInstance(resp, Award)
        self.assertEqual(AWARD_NAME, resp.__str__())
        self.assertEqual(AWARD_SHORT_NAME, resp.short_name)