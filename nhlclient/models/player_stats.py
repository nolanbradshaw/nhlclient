

class PlayerStats():
    def __init__(self, time_on_ice, assists, goals, penalty_mins,
                 shots, games, hits, power_play_goals, power_play_points,
                 power_play_time_on_ice, even_time_on_ice, faceoff_pct,
                 shot_pct, game_winning_goals, overtime_goals, shorthanded_goals,
                 shorthanded_points, shorthanded_time_on_ice, blocked_shots, 
                 plus_minus, points, shifts, time_on_ice_per_game,
                 even_time_on_ice_per_game, shorthanded_time_on_ice_per_game, 
                 power_play_time_on_ice_per_game):
        self.total_toi = time_on_ice
        self.assists = assists
        self.goals = goals
        self.penalty_minutes = penalty_mins
        self.shots = shots
        self.games = games
        self.hits = hits
        self.power_play_goals = power_play_goals
        self.power_play_points = power_play_points
        self.power_play_toi = power_play_time_on_ice
        self.event_strength_toi = even_time_on_ice
        self.faceoff_pct = faceoff_pct
        self.shot_pct = shot_pct
        self.game_winning_goals = game_winning_goals
        self.overtime_goals = overtime_goals
        self.short_handed_goals = shorthanded_goals
        self.short_handed_points = shorthanded_points
        self.short_handed_toi = shorthanded_time_on_ice
        self.blocked_shots = blocked_shots
        self.plus_minus = plus_minus
        self.points = points
        self.shifts = shifts
        self.toi_per_game = time_on_ice_per_game
        self.even_toi_per_game = even_time_on_ice_per_game
        self.short_handed_toi_per_game = shorthanded_time_on_ice_per_game
        self.power_play_toi_per_game = power_play_time_on_ice_per_game
        