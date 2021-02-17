from .base import NHLBase

class Team(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.full_name = self.data.get('name', '')
        self.team_name = self.data.get('teamName')
        self.site_url = self.data.get('officialSiteUrl')
        
    def __str__(self):
        return self.full_name