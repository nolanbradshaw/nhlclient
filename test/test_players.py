import unittest
from nhlclient import players
from nhlclient.models.goalie_stats import GoalieStats
from nhlclient.models.player_stats import PlayerStats
from nhlclient.models.player import Player

class TestPlayers(unittest.TestCase):
    def test_get_players_by_id(self):
        response = players.get_by_id(8476329)
        self.assertIsInstance(response, Player)
            
    def test_get_players_by_id_not_found(self):
        self.assertRaises(ValueError, players.get_by_id, -1)
        
    def test_get_goalie_season_stats(self):
        response = players.get_goalie_season_stats(8480382, '20202021')
        self.assertIsInstance(response, GoalieStats)
        
    def test_get_goalie_season_stats_not_found(self):
        # Sidney Crosby in a season he did not play in.
        self.assertRaises(ValueError, players.get_goalie_season_stats, 8471675, '19901901')
        
    def test_get_goalie_season_stats_wrong_type(self):
        # Sidney Crosby
        self.assertRaises(TypeError, players.get_goalie_season_stats, 8471675, '20192020')
        
    def test_get_player_sesason_stats(self):
        response = players.get_player_season_stats(8471675, '20202021')
        self.assertIsInstance(response, PlayerStats)