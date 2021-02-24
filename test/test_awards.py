import unittest
from nhlclient import awards
from nhlclient.constants import AWARDS
from nhlclient.models.award import Award

# Constants
AWARD_NAME = 'Stanley Cup'
AWARD_ID = AWARDS[AWARD_NAME]

class TestAwards(unittest.TestCase):
    def test_get(self):
        resp = awards.get()

        self.assertIsInstance(resp, list)
        self.assertTrue(resp)
        self.assertIsInstance(resp[0], Award)
        
    def test_get_by_id(self):
        resp = awards.get(AWARD_ID)

        self.assertIsInstance(resp, Award)
        self.assertEqual(AWARD_NAME, resp.__str__())