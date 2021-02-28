import unittest
from nhlclient.players import Players

# Constants
PLAYER_ID = 8471675
PLAYER_NAME = 'Sidney Crosby'
PLAYER_JERSEY_NUM = '87'
PLAYER_POSITION = 'Center'


class TestPlayers(unittest.TestCase):
    def test_get(self):
        result = Players().get(PLAYER_ID)
        
        self.assertTrue(len(result['people']) == 1)
        self.assertTrue(
            result['people'][0]['fullName'] == PLAYER_NAME
        )
        self.assertTrue(
            result['people'][0]['primaryNumber'] == PLAYER_JERSEY_NUM
        )