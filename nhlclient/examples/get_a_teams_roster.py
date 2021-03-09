import nhlclient
from nhlclient import constants

TEAM_ID = constants.TEAMS['TOR']

client = nhlclient.NhlClient()
# The id needs to be passed as list
# If no team is passed all teams rosters are returned
team_roster = client.team_rosters([TEAM_ID])

print(team_roster['teams'][0]['roster']['roster'][0]['person']['fullName'])