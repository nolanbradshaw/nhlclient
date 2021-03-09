import nhlclient

# NOTE: You can get player ids from client.team_rosters([TEAM_ID]).

# Sidney Crosby
PLAYER_ID = 8471675

client = nhlclient.NhlClient()

player = client.player(PLAYER_ID)
print(player['people'][0]['fullName'])
