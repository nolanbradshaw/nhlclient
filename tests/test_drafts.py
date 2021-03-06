import unittest
import nhlclient

DRAFT_YEAR = 2016
FIRST_PICK_NAME = 'Auston Matthews'


class TestDrafts(unittest.TestCase):
    def test_by_year(self):
        result = nhlclient.NhlClient().draft_year(DRAFT_YEAR)
        
        self.assertTrue(
            result['drafts'][0]['rounds'][0]['picks'][0]['prospect']['fullName'] 
            == FIRST_PICK_NAME
        )
