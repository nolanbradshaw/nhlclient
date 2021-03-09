import nhlclient

# NOTE: You can get player ids from team rosters.

# Sidney Crosby
PLAYER_ID = 8471675

client = nhlclient.NhlClient()
player = client.player_career_stats(PLAYER_ID)

# 'splits' is an array containing an object for each season.
# This endpoint can return stats from other leagues as well (NSMHL, OHL, etc).
print(player['stats'][0]['splits'][0]['season'])
print(player['stats'][0]['splits'][0]['stat']['goals'])