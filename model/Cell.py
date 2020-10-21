# This class will represent the cells in the matrix

class Cell:

    # Player 1 strategy
    P1Strat: int

    # Player 2 strategy
    P2Strat: int

    # Weight
    Weight: int

    # constructor
    def __init__(self, P1Strat: int, P2Strat: int, Weight: int):
        self.P1Strat = P1Strat
        self.P2Strat = P2Strat
        self.Weight = Weight

    # defaults constructor
    def __init__(self):
        self.P1Strat = 0
        self.P2Strat = 0
        self.Weight = 1

    # change p1 strat
    def changeP1(self, strat: int):

        self.P1Strat = strat

    # change p2 strat
    def changeP2(self, strat: int):

        self.P2Strat = strat

    # change weight of strategy
    def changeWeight(self, newWeight: int):

        self.Weight = newWeight

   # change p1 and p2 strategies simultaneously

    def changeP1AndP2(self, p1Strat: int, p2Strat: int):
        self.P1Strat= p1Strat
        self.P1Strat = p2Strat


