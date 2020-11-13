
import quantumrandom
from model.Matrix import Matrix
from model import Cell


# This class creates all the different iterations of the game matrix
class MatrixUpdater:
    startState: Matrix
    iterations: int
    states = []

    # Make whatever kind of iterator or matrix you want
    def __init__(self, startState: Matrix, iterations: int):

        self.startState = startState
        self.iterations = iterations

    # default matrix creator
    def __init__(self):

        self.iterations = 10

        m = Matrix("default", 4, 4, 0.0, 0.0)
        m.makeMatrix()

        self.startState = m

    # get iterations
    def getIterations(self):

        return self.iterations


    # updates matrix according to number of iterations
    def itter(self, m1: Matrix):



        i = 0

        while i < self.iterations:
            self.states.append(m1)
            self.makeStates(m1)
            i += 1

    # updates the matrix once
    def makeStates(self, m1: Matrix):

        e1 = m1.getEpsilon
        m1.makeMatrix()



        u = quantumrandom.randfloat(0, 1)

        list1 = m1.getL2

        d = m1.getDelta()

        delt = 1 - d


        # if no error
        if u > e1:
            self.setCellRange()

            v = quantumrandom.randfloat(0, 1)




            for list in list1:
                for cell1 in list:
                    if v >= cell1.getMin() and v < cell1.getMax():
                        currWeight = cell1.getWeight
                        increase = cell1.getp1strat
                        newWeight = currWeight + increase
                        cell1.setWeight(newWeight)
                    else:
                        w = cell1.getWeight()

                        cell1.setWeight(w * delt)

        # if error
        if u <= e1:
            x = m1.getRows
            y = m1.getCols

            cellX = quantumrandom.randint(0, x)
            cellY = quantumrandom.randint(0, y)

            l = m1.getL2()[cellX]
            choiceCell = l[cellY]

            currWeight = choiceCell.getWeight
            increase = choiceCell.getp1strat
            newWeight = currWeight + increase

            for lis in list1:
                for cel in lis:

                    w = cel.getWeight()

                    cel.setWeight(w * delt)


            choiceCell.setWeight(newWeight)



    # updates all the weights according to 1-delta

    # Assigns each cell a consecutive range to more easily calculate probabilities
    def setCellRange(self):
        # i = number of rows
        i = self.startState.getl2.length()
        j = 0
        while j < i:
            l = self.startState.getl2()[j]
            j += 1
            # k = number of columns
            k = l.length()
            m = 0
            while m < k:
                cell = l[m]
                if m == 0:
                    cell.setMin(0)
                    cell.setMax(cell.getProb())
                else:
                    # set cells other than the first to their probability range
                    lastCell = l[m - 1]
                    cell.setMin(lastCell.getMax())
                    currentMin = cell.setMin(lastCell.getMax())
                    cell.setMax(currentMin + cell.getProb())
                m += 1
