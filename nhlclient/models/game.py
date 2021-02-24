from .base import NHLBase
from .simplified_team import SimplifiedTeam
from .game_status import GameStatus
    
class Game(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        
        self.id = self.data.get('games')[0].get('gamePk')
        self.date = self.data.get('date')
        self.season = self.data.get('games')[0].get('season')
        self.status = GameStatus(self.data.get('games')[0].get('status', {}))
        
        self.away_team = SimplifiedTeam(self.data.get('games')[0].get('teams', {}).get('away', {}).get('team'))
        self.home_team = SimplifiedTeam(self.data.get('games')[0].get('teams', {}).get('home', {}).get('team'))
        
    def __str__(self):
        return f'{self.away_team} vs {self.home_team}'