from .base import NHLBase
from .position import Position
from .simplified_team import SimplifiedTeam

class FullPlayer(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        
        self.id = self.data.get('id')
        self.full_name = self.data.get('fullName')
        self.first_name = self.data.get('firstName')
        self.last_name = self.data.get('last_name')
        self.jersey_number = self.data.get('primaryNumber')
        
        self.birth_date = self.data.get('birthDate')
        self.age = self.data.get('currentAge')
        self.birth_city = self.data.get('birthCity')
        self.birth_state = self.data.get('birthStateProvince')
        self.birth_country = self.data.get('birthCountry')
        self.nationality = self.data.get('nationality')
        
        self.height = self.data.get('height')
        self.weight = self.data.get('weight')
        
        self.is_alternate_captain = self.data.get('alternateCaptain')
        self.is_captain = self.data.get('captain')
        self.is_rookie = self.data.get('rookie')
        self.active = self.data.get('active')
        self.handedness = self.data.get('shootsCatches')
        self.position = Position(self.data.get('primaryPosition', {}))
        self.team = SimplifiedTeam(self.data.get('currentTeam', {}))
    
    def __str__(self):
        return self.full_name