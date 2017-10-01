class TournamentPoints:
    def __init__(self, player):
        self.player = player
        self.points = []
        self.won_in_a_row = 0

    def add_win(self, berserk):
        self.won_in_a_row += 1
        if self.won_in_a_row <= 2:
            self.points.append(2 + berserk)
        else:
            self.points.append(4 + berserk)

    def add_draw(self):
        if self.won_in_a_row <= 2:
            self.points.append(1)
        else:
            self.points.append(2)
        self.won_in_a_row = 0

    def add_loss(self):
        self.points.append(0)
        self.won_in_a_row = 0
    
    def sum(self):
        return sum(self.points)