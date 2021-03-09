import nhlclient
from nhlclient import constants

TEAM_ID = constants.TEAMS['TOR']

client = nhlclient.NhlClient()
team_roster = client.team_roster(TEAM_ID)

print(team_roster['teams'][0]['roster']['roster'][0]['person']['fullName'])