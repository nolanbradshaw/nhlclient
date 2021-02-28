import unittest
from nhlclient.drafts import Drafts

DRAFT_YEAR = 2016
FIRST_PICK_NAME = 'Auston Matthews'


class TestDrafts(unittest.TestCase):
    def test_by_year(self):
        result = Drafts().by_year('2016')
        
        self.assertTrue(
            result['drafts'][0]['rounds'][0]['picks'][0]['prospect']['fullName'] 
            == FIRST_PICK_NAME
        )
