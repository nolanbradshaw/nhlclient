from .base import NHLBase
from .team import Team
from .prospect import Prospect

class Draft(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.round = self.data.get('round')
        self.overall = self.data.get('pickOverall')
        self.team = Team(self.data.get('team', {}))
        self.prospect = Prospect(self.data.get('prospect', {}))
    
    def __str__(self):
        return self.prospect.name