import unittest
import nhlclient

class TestSchedule(unittest.TestCase):
    def test_schedule(self):
        result = nhlclient.NhlClient().schedule()