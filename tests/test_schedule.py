import unittest
from nhlclient.schedule import Schedule

class TestSchedule(unittest.TestCase):
    def test_by_date(self):
        result = Schedule().by_date('2021-02-26')
        
        self.assertTrue(result['totalGames'] == 3)
        self.assertTrue(result['totalItems'] == 3)