from .base import NHLBase

class Venue(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.name = self.data.get('name')