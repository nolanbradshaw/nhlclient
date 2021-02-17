from .base import NHLBase
from .position import Position

class Roster(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('person').get('id')
        self.full_name = self.data.get('person').get('fullName', '')
        self.position = Position(self.data.get('position', {}))
        self.jersey_number = self.data.get('jersey_number')
        
    def __str__(self):
        return self.full_name