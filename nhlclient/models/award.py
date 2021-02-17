from .base import NHLBase

class Award(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.name = self.data.get('name', '')
        self.short_name = self.data.get('shortName')
        self.description = self.data.get('description')
        self.recipient_type = self.data.get('recipientType')
        self.history = self.data.get('history')
        self.image_url = self.data.get('imageUrl')
        self.home_url = self.data.get('homePageUrl')
        
    def __str__(self):
        return self.name