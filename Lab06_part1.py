import datetime
"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure

players=('ronaldo','rooney','torres')
player_stats={datetime.date(2012,6,19):[players,(0,0,0,0)],datetime.date(2012,6,20):[players,(3,0,0,0)],datetime.date(2012,6,21):[players,(0,0,1,0)],datetime.date(2012,6,23):[players,(0,2,0,0)],datetime.date(2012,6,25):[players,(0,2,0,0)]}

## implement highest_score
def highest_score(player_stats):
        player_name=0;date_of_score=0;score=0
        for date in player_stats.viewkeys():
            i=0;
            for goal in player_stats[date][1]:
                if(goal>score):
                    date_of_score=date
                    score=goal
                    player_name=player_stats[date][0][i]    
                else:pass
                i+=1
        return (player_name,date_of_score,score)

print highest_score(player_stats)
print
## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    i=0
    for date in player_stats.keys():
        if(i==len(player_stats.keys())):
                i=len(player_stats.keys())-1
        pdate=player_stats.keys()[(player_stats.keys().index(date)-1)]
        if(player  in player_stats[date][0]):
            player_name=player
            index=player_stats[date][0].index(player)
            if(player_stats[date][1][index]>player_stats[pdate][1][index]):
                date_of_score=date
                score=player_stats[date][1][index]
            else:i+=1
        else:return 'None'
    return (score)
print highest_score_for_player(player_stats,'torres')
## implement highest_scorer
