from espn_api.football import League
import pandas as pd
import cookies
import json

#TODO:
# MAKE DATAFRAME
# HOST ON PI
# CREATE TIDBYT DISPLAY
# PULL PRIMARY COLOR FROM TEAM LOGOS
# DISPLAY W-L RECORD ON TUES/WEDS
# STANDING MAYBE?
#

league = League(league_id=1551725656, year=2023,
                swid=cookies.swid, espn_s2=cookies.espn_s2)
box_scores = league.box_scores()
print(league.standings())
to_print = ''

for i in range(3):
    to_print += box_scores[i].away_team.team_name + ' ' + str(box_scores[i].away_score) + ' @ ' + box_scores[
        i].home_team.team_name + ' ' + str(box_scores[i].home_score)
    if i < 2:
        to_print += ", "

print(to_print)
print(box_scores[0].home_team.logo_url)
