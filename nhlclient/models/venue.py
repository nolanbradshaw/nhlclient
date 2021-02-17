from .base import NHLBase

class Venue(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.name = self.data.get('name')
        self.city = self.data.get('city')