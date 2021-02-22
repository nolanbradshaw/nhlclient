# nhlclient
A wrapper for the undocumented NHL API.

#### Table of Contents  
- [Teams](#Teams)
- [Players](#Players)
- [Awards](#Awards)

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

team = teams.get(TEAMS['TOR'])
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
# Awards

## Get all awards
```py
from nhlclient import awards

awards_list = awards.get()
for award in awards_list:
  print(award.name)
```
Output:
```
Stanley Cup
Jack Adams Award
Lady Byng Memorial Trophy
Calder Memorial Trophy
Clarence S. Campbell Bowl
King Clancy Memorial Trophy
Conn Smythe Trophy
Hart Memorial Trophy
William M. Jennings Trophy
Bill Masterton Memorial Trophy
James Norris Memorial Trophy
Lester Patrick Trophy
Ted Lindsay Award
Presidents' Trophy
Maurice Richard Trophy
Art Ross Trophy
Frank J. Selke Trophy
Vezina Trophy
Prince of Wales Trophy
NHL Lifetime Achievement Award
NHL Foundation Player Award
Mark Messier NHL Leadership Award
NHL General Manager of the Year Award
E.J. McGuire Award of Excellence
```

## Get award by id
```py
from nhlclient import awards
from nhlclient.constants import AWARDS

award = awards.get_by_id(AWARDS['Stanley Cup'])
print(award.description)
```
Output:
```
History: The Stanley Cup, the oldest trophy competed for by professional athletes in North America, was donated by Frederick Arthur, Lord Stanley of Preston and son of the Earl of Derby, in 1893. Lord Stanley purchased the trophy for 10 guineas ($50 at that time) for presentation to the amateur hockey champions of Canada. Since 1906, when Canadian teams began to pay their players openly, the Stanley Cup has been the symbol of professional hockey supremacy. It has been contested only by NHL teams since 1926-27 and has been under the exclusive control of the NHL since 1947.
```
