import nhlclient
from nhlclient import constants

client = nhlclient.NhlClient()

team_stats = client.team_stats(constants.TEAMS['VAN'])
print(team_stats['stats'][0]['splits'][0]['stat']['goalsAgainstPerGame'])