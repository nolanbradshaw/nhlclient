
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
        self.jersey_number = json['jerseyNumber']
        self.position = json['position']['name']
        
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