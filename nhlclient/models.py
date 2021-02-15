
class TeamModel():
    def __init__(self, json):
        self.id = json['id']
        self.full_name = json['name']
        self.team_name = json['teamName']
        self.site_url = json['officialSiteUrl']
        # self.division = division
        # self.conference = conference
        # self.venue = venue
        
class PlayerModel():
    def __init__(self, json):
        self.id = json['person']['id']
        self.full_name = json['person']['fullName']
        
        if 'jerseyNumber' in json:
            self.jersey_number = json['jerseyNumber']
        else:
            self.jersey_number = 'N/A'
            
        self.position = json['position']['name']

class GameModel():
    def __init__(self, **kwargs):
        valid_keys = ['date', 'game_id', 'season', 'detailed_status', 
                      'away_team_id', 'away_team_name', 'away_team_score',
                      'home_team_id', 'home_team_name', 'home_team_score']
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

class DivisionModel():
    def __init__(self, id, name, **kwargs):
        self.id = id
        self.name = name

class ConferenceModel():
    def __init__(self, id, name, **kwargs):
        self.id = id
        self.name = name

class VenueModel():
    def __init__(self, name, city, **kwargs):
        self.name = name
        self.city = city