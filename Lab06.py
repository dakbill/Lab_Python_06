import datetime
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team
    def add_score(self,score):
        #self.scores.append(date)
        self.scores.append(score)
#even dates,odd scores
    def total_score(self):
        total=0
        for i in self.scores:
            total+=i
        #return sum(self.scores)
        return total
    def average_score(self):
        return float(self.total_score())/len(self.scores)
torres=Player('Fernando','Torres')
torres.add_score(0)
torres.add_score(0)
torres.add_score(1)
torres.add_score(0)
torres.add_score(1)
print torres.average_score()
print torres.total_score()
class Team:
    name=None
    league=None
    manager_name=None
    points=None
    players=[]
    def __init__(self,name,league,manager_name,point):
        self.name=name
        self.manager_name=manager_name
        self.league=league
        self.point=point
    def add_player(self,Player):
        self.players.append(Player)
    def __str__(self):
        return self.name
spain=Team('spain','euro2012','Del Bosque',21)
portugal=Team('portugal','euro2012','Cronaldo',23)
torres=Player('Fernando','Torres',spain)
cronaldo=Player('Cristiano','Ronaldo',portugal)
spain.add_player(torres)
portugal.add_player(cronaldo)
class Match:
    home_team=None
    away_team=None
    date=None
    home_scores={}
    away_scores={}
    def __init__(self,home_team,away_team,day):
        self.home_team=home_team
        self.away_team=away_team
        self.date=day
        for name in home_team.players:
            self.home_scores.update({name.last_name:0})
        for name in away_team.players:
            self.away_scores.update({name.last_name:0})
    def home_score(self):
        total=0
        for player in self.home_scores.keys():
            total+=self.home_scores[player]
        return total    
    def away_score(self):
        total=0
        for player in self.away_scores.keys():
             total+=self.away_scores[player]
        return total    
    def winner(self):
        if(self.home_score()>self.away_score()):
            return self.home_team
        elif(self.home_score()<self.away_score()):
            return self.away_team
        else:
            return 'draw'
    def add_score(self,Player,score):
        team=Player.team
        if(team==self.home_team):
            status=self.home_team
            (self.home_scores[Player.last_name])+=score
            
        elif(team==self.away_team):
            status=self.away_team
            (self.away_scores[Player.last_name])+=score
        else:
            status=None
euro_semi_final=Match(spain,portugal,datetime.date(2012,06,28))
euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(cronaldo,1)
euro_semi_final.add_score(torres,1)
print euro_semi_final.winner()
