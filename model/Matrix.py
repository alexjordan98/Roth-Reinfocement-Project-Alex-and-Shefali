from model.Cell import Cell


#This class will represent the matrices that will be used
class Matrix:

    name: str
    columns: int
    rows: int
    epsilon: float
    delta: float
    from typing import List
    l2: List[List[Cell]]
    from typing import List
    p1Weights: List[float]
    from typing import List
    p2Weights: List[float]


    # non-symmetrical constructor
    def __init__(self, name: str, columns: int, rows: int, epsilon: float, delta: float, l2: List[List[Cell]],
                 p1Weights: List[float],p2Weights: List[float]):

        self.name = name
        self.columns = columns
        self.rows = rows
        self.epsilon = epsilon
        self.delta = delta
        self.l2 = l2
        self.p1Weights = p1Weights
        self.p2Weights = p2Weights

    # Construct Matrix
    def makeMatrix(self):

        #c = Cell(1, 1, 0, 0, 0)

        x = 0



        while x < self.rows:
            y = 0

            l = []
            while y < self.columns:

                l.append(Cell(1, 1, 0, 0, 0))

                y+=1
            self.l2.append(l)
            x+=1




    # set the probabilities
    def initiateProbs(self):

        totalP1 = 0
        totalP2 = 0


        for f in self.p1Weights:
            totalP1+=f


        for f1 in self.p2Weights:
            totalP2+=f1

        i = 0


        while i < self.rows:
            j = 0
            #print(i)

            while j < self.columns:
                #print(self.l2)


                p1prob = self.p1Weights[i] / totalP1
                p2prob = self.p2Weights[j] / totalP2

                endprob = p1prob * p2prob


                #print(endprob)

                self.l2[i][j].setProb(endprob)
                #print(self.l2[i][j].getProb())

                j+=1
            i+=1





    # change name of matrix
    def setName(self, newName: str):

        self.name = newName

    # change name of matrix
    def getName(self):
        return self.name

    # change number of rows in matrix
    def setRows(self, newRows: int):

        self.rows = newRows

    # get rows
    def getRows(self):

        return self.rows

    # change number of columns in matrix
    def setCols(self, newCol: int):

        self.columns = newCol

    # get columns
    def getCols(self):

        return self.columns

    # change epsilon
    def setEpsilon(self, eps: int):
        self.epsilon = eps

    # get epsilon
    def getEpsilon(self):
        return self.epsilon

    # change delta
    def setDelta(self, delt: int):
        self.delta = delt

    # get delta
    def getDelta(self):
        return self.delta

    #get l2
    def getL2(self):
        return self.l2;

    #set L2
    def setL2(self, new: List[List[Cell]]):

        self.l2 = new


    #Get p2Weights
    def getp2Weights(self):
        return self.p2Weights

    #setp2weights
    def setp2Weights(self, lis: List):
        self.p2Weights = lis

    # Get p1Weights
    def getp1Weights(self):
        return self.p1Weights

    # setp1weights
    def setp1Weights(self, lis: List):
        self.p1Weights = lis






