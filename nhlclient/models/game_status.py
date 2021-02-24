from .base import NHLBase

class GameStatus(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.state = self.data.get('detailedState', '')
    
    def __str__(self):
        return self.state