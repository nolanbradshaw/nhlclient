from .base import NHLBase

class PlayerStats(NHLBase):
    def __init__(self, data):
        NHLBase.__init__(self, data)
        self.time_on_ice = self.data.get('timeOnIce'),
        self.assists = self.data.get('assists'),
        self.goals = self.data.get('goals'),
        self.penalty_mins = self.data.get('pim'),
        self.shots = self.data.get('shots'),
        self.games = self.data.get('games'),
        self.hits = self.data.get('hits'),
        self.power_play_goals = self.data.get('powerPlayGoals'),
        self.power_play_points = self.data.get('powerPlayPoints'),
        self.power_play_time_on_ice = self.data.get('powerPlayTimeOnIce'),
        self.even_time_on_ice = self.data.get('evenTimeOnIce'),
        self.faceoff_pct = self.data.get('faceOffPct'),
        self.shot_pct = self.data.get('shotPct'),
        self.game_winning_goals = self.data.get('gameWinningGoals'),
        self.overtime_goals = self.data.get('overTimeGoals'),
        self.shorthanded_goals = self.data.get('shortHandedGoals'),
        self.shorthanded_points = self.data.get('shortHandedPoints'),
        self.shorthanded_time_on_ice = self.data.get('shortHandedTimeOnIce'),
        self.blocked_shots = self.data.get('blocked'),
        self.plus_minus = self.data.get('plusMinus'),
        self.points = self.data.get('points'),
        self.shifts = self.data.get('shifts'),
        self.time_on_ice_per_game = self.data.get('timeOnIcePerGame'),
        self.even_time_on_ice_per_game = self.data.get('evenTimeOnIcePerGame'),
        self.shorthanded_time_on_ice_per_game = self.data.get('shortHandedTimeOnIcePerGame'),
        self.power_play_time_on_ice_per_game = self.data.get('powerPlayTimeOnIcePerGame')
        # Goalie specific stats
        self.shutouts = self.data.get('shutouts')
        self.wins = self.data.get('wins')
        self.losses = self.data.get('losses')
        self.saves = self.data.get('saves')
        self.power_play_saves = self.data.get('powerPlaySaves')
        self.shorthanded_saves = self.data.get('shortHandedSaves')
        self.shorthanded_shots = self.data.get('shortHandedShots')
        self.even_strength_saves = self.data.get('evenSaves')
        self.even_strength_shots = self.data.get('evenShots')
        self.power_play_shots = self.data.get('powerPlayShots')
        self.save_pct = self.data.get('savePercentage')
        self.goal_against_avg = self.data.get('goalAgainstAverage')
        self.games_started = self.data.get('gamesStarted')
        self.shots_against = self.data.get('shotsAgainst')
        self.goals_against = self.data.get('goalsAgainst')
        self.power_play_save_pct = self.data.get('powerPlaySavePercentage')
        self.shorthanded_save_pct = self.data.get('shortHandedSavePercentage')
        self.even_strength_save_pct = self.data.get('evenStrengthSavePercentage')
        
        