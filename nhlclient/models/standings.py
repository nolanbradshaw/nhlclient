from .base import NHLBase
from .simplified_team import SimplifiedTeam

class Standings(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        
        self.team = SimplifiedTeam(self.data.get('team', {}))
        
        self.goals_against = self.data.get('goalsAgainst')
        self.goals_scored = self.data.get('goalsScored')
        self.games_played = self.data.get('gamesPlayed')
        
        self.regulation_wins = self.data.get('regulationWins')
        self.points = self.data.get('points')
        self.points_pct = self.data.get('pointsPercentage')
        
        self.power_play_rank = self.data.get('ppLeagueRank')
        self.division_rank = self.data.get('divisionRank')
        self.conference_rank = self.data.get('conferenceRank')
        self.league_rank = self.data.get('leagueRank')
        self.wild_card_rank = self.data.get('wildCardRank')
        
        # Streak