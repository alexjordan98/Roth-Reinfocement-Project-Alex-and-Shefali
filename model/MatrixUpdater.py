import quantumrandom
from model import Matrix
#This class creates all the different iterations of the game matrix
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

    # Assigns each cell a consecutive range to more easily calculate probabilities
    def setCellRange(self):
        # i = number of rows
        i = self.matrix.getl2.length()
        j = 0
        while j < i :
           l =  self.matrix.getl2()[j]
           j+=1
           # k = number of columns
           k = l.length()
           m = 0
           while m < k :
               cell = l[m]
               if m == 0:
                   cell.setMin(0)
                   cell.setMax(cell.getProb())
               else :
                   #set cells other than the first to their probability range
                   lastCell = l[m-1]
                   cell.setMin(lastCell.getMax())
                   currentMin = cell.setMin(lastCell.getMax())
                   cell.setMax(currentMin + cell.getProb())


