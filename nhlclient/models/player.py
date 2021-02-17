        
class Player():
    def __init__(self, json):
        self.id = json['id'],
        self.full_name = json['fullName'],
        self.position = json['primaryPosition']['name'],
        self.jersey_number = json['primaryNumber'],
        self.birth_date = json['birthDate'],
        self.age = json['currentAge'],
        self.birth_city = json['birthCity'],
        self.birth_state = json['birthStateProvince'],
        self.birth_country = json['birthCountry'],
        self.nationality = json['nationality'],
        self.height = json['height'],
        self.weight = json['weight'],
        self.is_alternate_captain = json['alternateCaptain'],
        self.is_captain = json['captain'],
        self.is_rookie = json['rookie'],
        self.handedness = json['shootsCatches'],
        self.current_team_id = json['currentTeam']['id']