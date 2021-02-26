from .base import NHLBase
from .game import Game

class Schedule(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.date = self.data.get('date')
        self.total_games = self.data.get('totalGames')
        self.games = [Game(game) for game in self.data.get('games', [])]