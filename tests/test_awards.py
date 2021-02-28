import unittest
from nhlclient.awards import Awards
from nhlclient.constants import AWARDS

# Constants
AWARD_NAME = 'Stanley Cup'
AWARD_ID = AWARDS[AWARD_NAME]

class TestAwards(unittest.TestCase):
    def test_all(self):
        result = Awards().all()
        
        self.assertTrue(len(result['awards']) == 25)
        
    def test_get(self):
        result = Awards().by_id(AWARD_ID)
        
        self.assertTrue(
            result['awards'][0]['name'] == AWARD_NAME
        )