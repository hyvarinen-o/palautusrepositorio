

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.terms = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_tied_score(self):
        if self.m_score1 >= 3:
            return "Deuce"
        return f"{self.terms[self.m_score1]}-All"
    
    def get_score_over_four(self):
        minus_score = self.m_score1 - self.m_score2
        if minus_score == 1:
            return "Advantage player1"
        if minus_score == -1:
            return "Advantage player2"
        if minus_score >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_tied_score()

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_over_four()

        return f"{self.terms[self.m_score1]}-{self.terms[self.m_score2]}"