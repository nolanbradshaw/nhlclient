from .base import NHLBase

class Season(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.id = self.data.get('seasonId')
        self.start_date = self.data.get('regularSeasonStartDate')
        self.regular_season_end_date = self.data.get('regularSeasonEndDate')
        self.end_date = self.data.get('seasonEndDate')
        
        self.num_games = self.data.get('numberOfGames')
        self.olympics_participation = self.data.get('olympicsParticipation')
        
        self.conferences_used = self.data.get('conferencesInUse')
        self.divisions_used = self.data.get('divisionsInUse')
        self.wild_card_used = self.data.get('wildCardInUse')
        
    def __str__(self):
        return self.id