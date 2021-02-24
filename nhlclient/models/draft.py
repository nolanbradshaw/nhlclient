from .base import NHLBase
from .prospect import Prospect
from .simplified_team import SimplifiedTeam

class Draft(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.round = self.data.get('round')
        self.overall = self.data.get('pickOverall')
        self.team = SimplifiedTeam(self.data.get('team', {}))
        self.prospect = Prospect(self.data.get('prospect', {}))
    
    def __str__(self):
        return self.prospect.name