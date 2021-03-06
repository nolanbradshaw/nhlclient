import unittest
import nhlclient

# Constants
AWARD_NAME = 'Stanley Cup'
AWARD_ID = nhlclient.AWARDS[AWARD_NAME]

class TestAwards(unittest.TestCase):
    def test_awards(self):
        result = nhlclient.NhlClient().awards()
        
        self.assertTrue(len(result['awards']) == 25)
        
    def test_award(self):
        result = nhlclient.NhlClient().award(AWARD_ID)
        
        self.assertTrue(
            result['awards'][0]['name'] == AWARD_NAME
        )