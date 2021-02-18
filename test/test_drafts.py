import unittest
from nhlclient import drafts
from nhlclient.models.draft import Draft

class TestDrafts(unittest.TestCase):
    def test_get_draft_by_year(self):
        resp = drafts.get_draft_by_year(2013)
        self.assertTrue(resp)
        self.assertIsInstance(resp, list)
        self.assertIsInstance(resp[0], Draft)
        
    def test_get_draft_by_year_not_found(self):
        self.assertRaises(ValueError, drafts.get_draft_by_year, 1000)