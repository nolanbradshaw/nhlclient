        
class Player():
    def __init__(self, id, full_name, position, jersey_number, birth_date,
                 age, birth_city, birth_state, birth_country, nationality,
                 height, weight, is_alternate_captain, is_captain, is_rookie,
                 handedness, current_team_id):
        self.id = id
        self.full_name = full_name
        self.position = position
        self.jersey_number = jersey_number
        self.birth_date = birth_date
        self.age = age
        self.birth_city = birth_city
        self.birth_state = birth_state
        self.birth_country = birth_country,
        self.nationality = nationality
        self.height = height
        self.weight = weight
        self.is_alternate_captain = is_alternate_captain
        self.is_captain = is_captain
        self.is_rookie = is_rookie
        self.handedness = handedness
        self.current_team_id = current_team_id