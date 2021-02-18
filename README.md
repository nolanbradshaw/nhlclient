# nhlclient
A wrapper for the undocumented NHL API.

#### Table of Contents  
- [Teams](#Teams)
- [Players](#Players)

# Teams

## Get all teams
```py
from nhlclient import teams

teams = teams.get()
for team in teams:
  print(team.full_name)
```
Output:
```
New Jersey Devils
New York Islanders
New York Rangers
Philadelphia Flyers
Pittsburgh Penguins
Boston Bruins
Buffalo Sabres
Montréal Canadiens
Ottawa Senators
Toronto Maple Leafs
Carolina Hurricanes
Florida Panthers
Tampa Bay Lightning
Washington Capitals
Chicago Blackhawks
Detroit Red Wings
Nashville Predators
St. Louis Blues
Calgary Flames
Colorado Avalanche
Edmonton Oilers
Vancouver Canucks
Anaheim Ducks
Dallas Stars
Los Angeles Kings
San Jose Sharks
Columbus Blue Jackets
Minnesota Wild
Winnipeg Jets
Arizona Coyotes
Vegas Golden Knights
```

## Get team by id
```py
from nhlclient import teams
from nhlclient.constants import TEAMS

team = teams.get_by_id(TEAMS['TOR'])
print(team.record.points_pct, team.record.points)
```
Output:
```
0.7647058823529411 26
```

## Get a teams roster
```py
from nhlclient import teams
from nhlclient.constants import TEAMS

roster = teams.get_roster_by_id(TEAMS['TOR'])
for player in roster:
  print(player.full_name)
```
Output:
```
Wayne Simmonds
Jack Campbell
Rasmus Sandin
Alexander Barabanov
Joe Thornton
Jason Spezza
Jake Muzzin
Zach Bogosian
Michael Hutchinson
TJ Brodie
John Tavares
Justin Holl
Zach Hyman
Frederik Andersen
Travis Boyd
Morgan Rielly
Jimmy Vesey
Alexander Kerfoot
Nic Petan
William Nylander
Pierre Engvall
Travis Dermott
Mitchell Marner
Auston Matthews
Joseph Woll
Ilya Mikheyev
Mikko Lehtonen
```

# Players

## Get a player by id
- Get basic player information by id
```py
from nhlclient import players

player = players.get_by_id(8471675)
print(player.full_name)
print(player.jersey_number)
print(player.age)
print(player.is_captain)
print(player.team.full_name)
```
Output:
```
Sidney Crosby
87
33
True
Pittsburgh Penguins
```

## Get season stats
- Get a players stats for a specific season
```py
from nhlclient import players

player_stats = players.get_season_stats(8471675, '20162017')
print(player_stats.time_on_ice)
print(player_stats.games)
print(player_stats.goals, player_stats.assists)
print(player_stats.hits)
```
Output:
```
1490:50
75   
44 45
80
```
