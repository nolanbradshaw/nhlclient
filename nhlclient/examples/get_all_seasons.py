import nhlclient

client = nhlclient.NhlClient()

seasons_list = client.seasons()
for season in seasons_list['seasons']:
    print(season['regularSeasonStartDate'])