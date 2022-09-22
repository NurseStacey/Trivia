from dataclasses import dataclass

from numpy import append

@dataclass
class One_Team_Class():
    score:int
    name:str
    win_score:int
    lose_score:int
    team_number: int

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
    
    def set_win_score(self,score):
        self.win_score = score

    def set_lose_score(self, score):
        self.lose_score = score

class The_Game_Class():

    def __init__(self):
        self.number_teams=0
        self.teams = []
        self.control = -1
        self.which_question = 0

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
            self.teams.append(One_Team_Class(
                0, 'Team ' + str(index+1), 0, 0, index))

    def set_team_name(self, which, team_name):
        self.teams[which].name=team_name

    def calculate_scores(self, difficulty):

        self.teams.sort(key=lambda x: x.score, reverse=True)
        score_total = 0
        for one_team in self.teams:
            score_total += one_team.score

        
        # difference_between_big_small = self.teams[0].score - self.teams[self.number_teams-1].score
        top_score = self.teams[0].score
        # win_score = []
        # lose_score = []

        for one_team in self.teams:
            this_score = 100 * (1.02 ** self.which_question) * (1+.4*(difficulty-1))
            this_score  += (0.4 * (top_score - one_team.score))
            one_team.set_win_score(int(this_score))

        
        self.teams.sort(key=lambda x: x.score, reverse=False)
        low_score = self.teams[0].score

        for one_team in self.teams:
            this_score = (one_team.score-low_score)*.4
            one_team.set_lose_score(-int(this_score))

        # best_score = self.teams[0].score
        # worse_score = self.teams[self.number_teams-1].score
        # base_score = max(100, int(score_total*.03))*difficulty

        # for index, one_team in enumerate(self.teams):
        #     win_score.append(base_score * (1+index*(best_score-worse_score)*.05))
        #     lose_score.append(max(one_team.score,(best_score-worse_score)*.1*(self.number_teams-index)))

        # for index1 in range(self.number_teams):
        #     for index2 in range(index1):
        #         if (win_score[index1]+self.teams[index1].score) > (1.25*(win_score[index2]+self.teams[index2].score)):
        #             win_score[index1] = (
        #                 1.25*(win_score[index2]+self.teams[index2].score)) - self.teams[index1].score

        #         if (self.teams[index1].score-lose_score[index1]) < (1.1*(self.teams[index2].score-lose_score[index2])):
        #             lose_score[index1] = 1.1 * \
        #                 (self.teams[index2].score-lose_score[index2]) - \
        #                 self.teams[index1].score


        # #in case there is a tie


        # for index1 in reversed(range(len(self.teams))):
        #     for index2 in range(index1):
        #         if self.teams[index1].score==self.teams[index2].score:
        #             win_score[index2] = win_score[index1]

        # for index1 in range(len(self.teams)):
        #     for index2 in range(index1):
        #         if self.teams[index1].score == self.teams[index2].score:
        #             lose_score[index2] = lose_score[index1]

        # for index in range(len(self.teams)):
        #     self.teams[index].set_scores(
        #         int(win_score[index]), int(-1*lose_score[index]))


        ##My first try
        # score_total = 0
        # Best_Score = 0
        # for one_team in self.teams:
        #     score_total += one_team.score
        #     Best_Score = max(Best_Score,one_team.score)

        # base_score = max(100, int(score_total*.36))*difficulty

        # for one_team in self.teams:
        #     score_lower = 0
        #     score_higher = 0

        #     for other_team in self.teams:


        #         #find the scores closest to this team's score
        #         #not sure if I will use score_higher for something
        #         if other_team.score>one_team.score:
        #             if score_higher==0:
        #                 score_higher = other_team.score
        #             elif other_team.score<score_higher:
        #                 score_higher=one_team.score
                
        #         if other_team.score<one_team.score:
        #             if score_lower == 0:
        #                 score_lower = other_team.score
        #             elif other_team.score > score_lower:
        #                 score_lower = one_team.score

        #     if score_lower == 0:
        #         score_lower=one_team.score
        #     #this is for adjusting the amount they can win or lose
        #     #based on how far they are from the next players
        #     win_multiplier = 1 + \
        #         (max(0, Best_Score-one_team.score))*.3/max(1, score_total)
        #     lose_multiplier = 0 + \
        #         (one_team.score-score_lower)*.4/max(1, score_total)
        #     # win_multiplier = 1 + \
        #     #     (max(0, score_higher-one_team.score))*.3/max(1, score_higher)
        #     # lose_multiplier = 0 + \
        #     #     (one_team.score-score_lower)*.4/max(1, one_team.score)

        #     one_team.set_scores(
        #         int(base_score*win_multiplier), \
        #             -1*min(max(10,one_team.score)-10,int(base_score*lose_multiplier)))
        self.which_question += 1

        self.teams.sort(key=lambda x: x.team_number, reverse=False)


    def won(self, which):
        self.teams[which].won()

    def lost(self, which):
        self.teams[which].lost()

    def adjust_score(self, adjustment, which):

        self.teams[which].score += adjustment