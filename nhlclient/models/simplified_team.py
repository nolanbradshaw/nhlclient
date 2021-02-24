from .base import NHLBase

class SimplifiedTeam(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.full_name = self.data.get('name')
    
    def __str__(self):
        return self.full_name