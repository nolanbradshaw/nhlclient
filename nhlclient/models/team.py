from .base import NHLBase

class TeamRecord(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.regulation_wins = self.data.get('regulationWins')
        self.goals_against = self.data.get('goalsAgainst')
        self.goals_cored = self.data.get('goalsScored')
        self.points = self.data.get('points')
        self.division_rank = self.data.get('divisionRank')
        self.division_away_rank = self.data.get('divisionRoadRank')
        self.division_home_rank = self.data.get('divisionHomeRank')
        self.conference_rank = self.data.get('conferenceRank')
        self.conference_away_rank = self.data.get('conferenceRoadRank')
        self.conference_home_rank = self.data.get('conferenceHomeRank')
        self.games_played = self.data.get('gamesPlayed')
        self.points_pct = self.data.get('pointsPercentage')
        self.powerplay_division_rank = self.data.get('ppDivisionRank')
        self.powerplay_conference_rank = self.data.get('ppConferenceRank')
        self.powerplay_league_rank = self.data.get('ppLeagueRank')

class Team(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('id')
        self.full_name = self.data.get('name')
        self.team_name = self.data.get('teamName')
        self.site_url = self.data.get('officialSiteUrl', '')
        
        if self.data.get('record'):
            self.record = TeamRecord(self.data.get('record'))
        else:
            self.record = None
        
    def __str__(self):
        return self.full_name