from .base import NHLBase

class FullTeam(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        
        self.id = self.data.get('id')
        self.abbreviation = self.data.get('abbreviation')
        self.full_name = self.data.get('name')
        self.short_name = self.data.get('shortName')
        self.team_name = self.data.get('teamName')
        
        self.location_name = self.data.get('locationName')
        self.first_year = self.data.get('firstYearOfPlay')
        self.official_site = self.data.get('officialSiteUrl')
        self.active = self.data.get('active')
        
        # TODO: Add these to the class
        # Venue
        # Division
        # Conference
        # Franchise
        
    def __str__(self):
        return self.full_name