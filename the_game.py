from dataclasses import dataclass

@dataclass
class One_Team_Class():
    score:int
    name:str
    win_score:int
    lose_score:int

    def won(self):
        self.score += self.win_score

    def lost(self):
        self.score += self.lose_score

    def set_scores(self, win_score, lose_score):
        self.win_score=win_score
        self.lose_score=max(0-self.score,lose_score)

    def answered_right(self):
        self.win_score = int(self.win_score*.08)

    def answered_wrong(self):
        self.lose_score = int(self.lose_score*1.25)
        

class The_Game_Class():

    def __init__(self):
        self.number_teams=0
        self.teams = []
        self.control = -1

    def answered_wrong(self):
        for one_team in self.teams:
            one_team.answered_wrong()

    def answered_right(self):

        for one_team in self.teams:
            one_team.answered_right()

    def set_number_of_teams(self, number_teams):

        self.number_teams=number_teams 
        self.teams = []
        for index in range(self.number_teams):
            self.teams.append(One_Team_Class(0, 'Team ' + str(index+1), 0, 0))

    def set_team_name(self, which, team_name):
        self.teams[which].name=team_name

    def calculate_scores(self, difficulty):

        score_total = 0
        for one_team in self.teams:
            score_total += one_team.score

        base_score = max(100, int(score_total*.36))*difficulty

        for one_team in self.teams:
            score_lower = 0
            score_higher = 0

            for other_team in self.teams:

                if other_team.score>one_team.score:
                    if score_higher==0:
                        score_higher = other_team.score
                    elif other_team.score<score_higher:
                        score_higher=one_team.score
                
                if other_team.score<one_team.score:
                    if score_lower == 0:
                        score_lower = other_team.score
                    elif other_team.score > score_lower:
                        score_lower = one_team.score

            win_multiplier = 1 + \
                (max(0, score_higher-one_team.score))*.3/max(1, score_higher)
            lose_multiplier = 0 + \
                (one_team.score-score_lower)*.4/max(1, one_team.score)

            one_team.set_scores(
                int(base_score*win_multiplier), -1*int(base_score*lose_multiplier))


    def won(self, which):
        self.teams[which].won()

    def lost(self, which):
        self.teams[which].lost()
