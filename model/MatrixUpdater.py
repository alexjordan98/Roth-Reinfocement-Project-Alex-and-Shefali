import quantumrandom
from model import Matrix
#This class crreates all the different itterations of the game matrix
class MatrixUpdater:

    startState: Matrix
    iterations: int
    states = []

    #Make whatever kind of iterator or matrix you want
    def __init__(self, startState: Matrix, iterations: int):

        self.startState = startState
        self.iterations = iterations

    #default matrix creator
    def __init__(self):

        self.iterations = 10

        m = Matrix("default", 10, 0.0, 0.0)
        m.makeMatrix()

        self.startState = m

    # Creating new iterations
    def itter(self):
