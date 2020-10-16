
# This class will represent the cells in the matrix

class Cell:

    #Player 1 strategy
    P1Strat: int

    #Player 2 strategy
    P2Strat: int

    #Weight
    Weight: int

    #constructor
    def __init__(self, P1Strat: int, P2Strat: int, Weight: int):

        self.P1Strat = P1Strat
        self.P2Strat = P2Strat
        self.Weight = Weight

    #defaults constructor
    def __init__(self):

        self.P1Strat = 0
        self.P2Strat = 0
        self.Weight = 1