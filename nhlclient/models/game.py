from .base import NHLBase
from .team import Team

class GameStatus(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.state = self.data.get('detailedState', '')
    
    def __str__(self):
        return self.state
    
class Game(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.date = self.data.get('date')
        self.id = self.data.get('gamePk')
        self.season = self.data.get('season')
        self.away_team = Team(self.data.get('teams', {}).get('away', {}).get('team', {}))
        self.home_team = Team(self.data.get('teams', {}).get('home', {}).get('team', {}))
        self.status = GameStatus(self.data.get('status', {}))
        
    def __str__(self):
        return f'{self.away_team} vs {self.home_team}'