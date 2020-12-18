import quantumrandom
import copy
from model.Matrix import Matrix

from model.Cell import Cell


# This class creates all the different iterations of the game matrix
class MatrixUpdater:
    iterations: int
    from typing import List
    states: List[Matrix]


    # Make whatever kind of iterator or matrix you want
    def __init__(self, iterations: int, states: List[Matrix]):

        self.iterations = iterations
        self.states = states

    # updates matrix according to number of iterations
    def itter(self, m1: Matrix):


        m1.makeMatrix()
        self.makeStates(m1)
        self.states.append(m1)
        i = 0

        for i in range(self.iterations):
            toadd = Matrix("M" + str(i +1), 10, 10, 0, 1, [], [], [])
            print(i)

            if i != 0:


                self.coppyMatrix(self.states[i-1], toadd)

                self.makeStates(toadd)
                #print(toadd.name)

                self.states.append(toadd)
                #print(toadd.p1Weights)

                #self.states.append(self.makeStates(self.coppyMatrix(self.states[i-1]
                 #                                                   , Matrix("m" + str(i), 10, 10, 0, 1, [], [], []))))



        tes = 0

        while tes < self.iterations:

            print(self.states[tes])

            print(self.states[tes].name)

            print(self.states[tes].p1Weights)
            tes+=1

    # create matrix depending on inputted matrix
    def coppyMatrix(self, m1: Matrix, m2: Matrix):

        m2.setCols(m1.getCols())
        m2.setRows(m1.getRows())

        m2.setEpsilon(m1.getEpsilon())

        m2.setDelta(m1.getDelta())

        newl2 = copy.deepcopy(m1.getL2())
        print(newl2)
        m2.setL2(newl2)


        newp1 = copy.copy(m1.getp1Weights())
        newp2 = copy.copy(m1.getp2Weights())

        m2.setp1Weights(newp1)
        m2.setp2Weights(newp2)

        #return m2

    # copies a Matrix as in a list like this [][]
    def matrixHelp(self, mat: List[List[Cell]]):

        l2 = []

        for i in range(len(mat)):
            l1 = mat[i]
            l3 = []
            for j in range(len(l1)):
                c = copy.copy(l1[j])
                l3.append(c)





    # updates the matrix once
    def makeStates(self, m1: Matrix):

        e1 = m1.getEpsilon()


        m1.initiateProbs()



        u = float(quantumrandom.randint(0, 100000) / 100000)

        #list1 = list(m1.getL2())

        d = m1.getDelta()

        delt = float(1 - d)


        #print(u)

        #print(u>e1)

        # if no error
        if u > e1:
            self.setCellRange(m1)

            v = float(quantumrandom.randint(0, 100000) / 100000)

            x = 0

            #print(m1.l2[0][0].getMin())

            #for l in m1.l2:
                #for c in l:
                    #print(c.getMin())

            p1w = 0
            p2w = 0

            yplace = 0
            xplace = 0

            while x < m1.rows:
                y = 0

                while y < m1.columns:

                    # print(m1.l2[x][y].getMin())
                    if (m1.l2[x][y].getMin() < v) and (m1.l2[x][y].getMax() > v):
                        print(m1.l2[x][y].getMin() < v) and (m1.l2[x][y].getMax() > v)

                        p1w = m1.p1Weights[x] + m1.l2[x][y].getP1Strat()
                        p2w = m1.p2Weights[y] + m1.l2[x][y].getP2Strat()

                        xplace = x
                        yplace = y

                    y+=1
                x+=1

            q = 0
            r = 0
            while q < len(m1.p1Weights):
                m1.p1Weights[q] *= delt

                q+=1

            while r < len(m1.p2Weights):
                m1.p2Weights[r] *= delt
                r += 1

            m1.p1Weights[xplace] = p1w
            m1.p1Weights[yplace] = p2w

        else: #if u < e1:

            xx = m1.getRows() - 1
            yy = m1.getCols() - 1

            cellX = int(quantumrandom.randint(0, xx))
            cellY = int(quantumrandom.randint(0, yy))

            l = list(m1.getL2())
            m = list(l[cellX])

            choiceCell = m[cellY]

            p1add = choiceCell.getP1Strat()
            p2add = choiceCell.getP1Strat()

            a = 0
            b = 0

            m1.p1Weights[cellX] += p1add

            m1.p2Weights[cellY] += p2add

            while a < xx:

                if a != cellX:
                    m1.p1Weights[a] * delt

                a+=1

            while b < yy:

                if b != cellY:
                    m1.p2Weights[b] *delt

                b+=1





    # Assigns each cell a consecutive range to more easily calculate probabilities
    def setCellRange(self, m1: Matrix):

        x = 0


        while x < m1.getRows():
            y = 0

            while y < m1.getCols():

                prob = m1.l2[x][y].getProb()

                if (x == 0) and (y == 0):


                    m1.l2[x][y].setMin(0)
                    #print ( m1.l2[x][y].getMin())
                    m1.l2[x][y].setMax(prob)

                if (y == 0) and (x > 0):

                    c = x - 1
                    d = m1.columns - 1
                    mins = m1.l2[c][d].getMax()
                    m1.l2[x][y].setMin(mins)
                    #print(mins)
                    m1.l2[x][y].setMax(mins + prob)

                if (y > 0) and (x >= 0):

                    min = m1.l2[x][y-1].getMax()
                    #print(min)

                    m1.l2[x][y].setMin(min)
                    m1.l2[x][y].setMax(min + prob)

                y+=1
                #print(y)
            x+=1
            #print(x)



    # get iterations
    def getIterations(self):

        return self.iterations

    # get startState matrix
    def getStartState(self):
        return self.startState

    # get total weight, weight of cell on last iteration
    def getTotalWeight(self):

        return self.totalWeight


