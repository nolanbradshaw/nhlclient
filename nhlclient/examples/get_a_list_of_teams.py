import nhlclient
from nhlclient import constants

client = nhlclient.NhlClient()

teams_list = client.teams()
for team in teams_list['teams']:
    print(team['name'])


team_ids = [
    constants.TEAMS['TOR'],
    constants.TEAMS['MTL'],
    constants.TEAMS['OTT']
]

filtered_teams_list = client.teams(team_ids)
for team in filtered_teams_list['teams']:
    print(team['name'])