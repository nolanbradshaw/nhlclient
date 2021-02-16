
class Game():
    def __init__(self, date, game_id, season, detailed_status,
                 away_team_id, away_team_name, away_team_score,
                 home_team_id, home_team_name, home_team_score):
        self.date = date
        self.id = game_id
        self.season = season
        self.detailed_status = detailed_status
        self.away_team_id = away_team_id
        self.away_team_name = away_team_name
        self.away_team_score = away_team_score
        self.home_team_id = home_team_id
        self.home_team_name = home_team_name 
        self.home_team_score = home_team_score