from model.Cell import Cell

#This class will represent the matrices that will be used
class Matrix:

    name: str
    columns: int
    rows: int
    epsilon: float
    delta: float
    l2 = []

    # # symmetrical constructor
    # def __init__(self, name: str, columns: int, epsilon: float, delta: float):
    #
    #     self.name = name
    #     self.columns = columns
    #     self.rows = columns
    #     self.epsilon = epsilon
    #     self.delta = delta

    # non-symmetrical constructor
    def __init__(self, name: str, columns: int, rows: int, epsilon: float, delta: float):

        self.name = name
        self.columns = columns
        self.rows = rows
        self.epsilon = epsilon
        self.delta = delta

    # Construct Matrix
    def makeMatrix(self):

        c = Cell()

        y = self.columns
        x = self.rows

        l1 = []

        while x > 0:
            l1.append(c)
            x -= 1
        while y > 0:
            self.l2.append(l1)
            y -= 1

    # set the probabilities
    def initiateProbs(self):

        totals = 0


        for list in self.l2:
            for Cell in list:
                totals += Cell.getWeight()

        for list in self.l2:
            for Cell in list:
                Cell.createProbabilitiey(totals)



    # change name of matrix
    def setName(self, newName: str):

        self.name = newName

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

    # change episilon
    def setEpsilon(self, eps: int):
        self.epsilon = eps

    # get epislon
    def getEpislon(self):
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




