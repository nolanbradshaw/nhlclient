import unittest
from nhlclient import players
from nhlclient.models.player import Player

class TestPlayers(unittest.TestCase):
    def test_get_players_by_id(self):
            response = players.get_by_id(8476329)
            self.assertIsInstance(response, Player)
            
    def test_get_players_by_id_not_found(self):
        self.assertRaises(ValueError, players.get_by_id, -1)