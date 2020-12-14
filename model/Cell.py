import quantumrandom
import dataclasses


# This class will represent the cells in the matrix
#@dataclasses.dataclass(frozen=True)
class Cell:
    # Player 1 strategy
    P1Strat: float

    # Player 2 strategy
    P2Strat: float

    # Probability
    Probability: float

    # min, lower end of range of probability
    Min: float

    # max, higher end of range of range probability
    Max: float


    # constructor
    def __init__(self, P1Strat: float, P2Strat: float, Probability: float, Min: float, Max: float):
        self.P1Strat = P1Strat
        self.P2Strat = P2Strat
        self.Probability = Probability
        self.Min = Min
        self.Max = Max

    # defaults constructor
    def setdDefault(self):
        self.P1Strat = 0
        self.P2Strat = 0
        self.Min = 0;
        self.Max = 0;
        self.Weight = quantumrandom.randint(0, 6)
        self.Probability = float(quantumrandom.randint(0, 10) / 10)

    # change p1 strat
    def setP1Strat(self, strat: int):

        self.P1Strat = strat

    #get p1 strat
    def getP1Strat(self):

        return self.P1Strat

    # change p2 strat
    def setP2Strat(self, strat: int):

        self.P2Strat = strat

    # get p2 strat
    def getP2Strat(self):

        return self.P2Strat

    # set minimum range value for probability
    def setMin(self, newMin: float):

        self.Min = newMin

    # set maximum range value for probability
    def setMax(self, newMax: float):
        self.Max = newMax

    # get maximum value for probability range
    def getMax(self):

        return self.Max

    # get maximum value for probability range
    def getMin(self):

            return self.Min

    # change p1 and p2 strategies simultaneously
    def setP1AndP2(self, p1Strat: int, p2Strat: int):
        self.P1Strat= p1Strat
        self.P1Strat = p2Strat


    # get probability
    def getProb(self):
        return self.Probability

    # set probability
    def setProb(self, p: float):
        self.Probability = p




