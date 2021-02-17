from .base import NHLBase

class Position(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.code = self.data.get('code')
        self.name = self.data.get('name', '')
        self.type = self.data.get('type')
        self.abbreviation = self.data.get('abbreviation')
        
    def __str__(self):
        return self.name