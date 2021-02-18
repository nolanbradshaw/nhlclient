from .base import NHLBase

class Division(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.name = self.data.get('name', '')
        self.abbreviation = self.data.get('abbreviation')
        self.is_active = self.data.get('is_active')
        
    def __str__(self):
        return self.name