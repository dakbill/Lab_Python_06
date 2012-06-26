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
