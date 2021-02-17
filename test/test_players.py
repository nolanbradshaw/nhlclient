import unittest
from nhlclient import players
from nhlclient.models.player_stats import PlayerStats
from nhlclient.models.player import Player

class TestPlayers(unittest.TestCase):
    def test_get_players_by_id(self):
        response = players.get_by_id(8476329)
        self.assertIsInstance(response, Player)
            
    def test_get_players_by_id_not_found(self):
        self.assertRaises(ValueError, players.get_by_id, -1)
        
    def test_get_player_season_stats(self):
        response = players.get_season_stats(8471675, '20202021')
        self.assertIsInstance(response, PlayerStats)
        
    def test_get_player_season_stats_not_found(self):
        self.assertRaises(ValueError, players.get_season_stats, 0, '20202021')