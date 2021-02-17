from .base import NHLBase

class Player(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.full_name = self.data.get('fullName')
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
        self.handedness = self.data.get('shootsCatches')
        self.position_dict = self.data.get('primaryPosition', {})
        self.current_team_dict = self.data.get('currentTeam', {})
        
    @property
    def position_name(self):
        return self.position_dict.get('name')
    
    @property
    def current_team_id(self):
        return self.current_team_dict.get('id')
    
    @property
    def current_team_name(self):
        return self.current_team_dict.get('name')