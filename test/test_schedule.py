import unittest
from nhlclient import schedule
from nhlclient.models.schedule import Schedule

class TestSchedule(unittest.TestCase):
    def test_by_date(self):
        resp = schedule.get_by_date('2021-02-26')
        
        self.assertIsInstance(resp, Schedule)
        self.assertFalse(resp.date is None)
        self.assertFalse(resp.total_games is None)
        
    def test_by_date_error(self):
        self.assertRaises(ValueError, schedule.get_by_date, None)