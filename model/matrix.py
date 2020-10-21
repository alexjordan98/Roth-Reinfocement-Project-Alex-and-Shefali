import numpy as np
import Cell.py

#This class will represent the matrices that will be used
class Matrix:

    name: str
    columns: int
    rows: int

    # symmetrical constructor
    def __init__(self, name: str, columns: int):

        self.name = name
        self.columns = columns
        self.rows = columns

    # non-symmetrical constructor
    def __init__(self, name: str, columns: int, rows: int):

        self.name = name
        self.columns = columns
        self.rows = rows

    # Construct Matrix
    def makeMatrix(self):

        c = Cell()

        y = self.columns
        x = self.rows

        l1 = []
        l2 = []


        while y > 0:
            l1.append(c)
        while x > 0:
            l2.append(l1)

    # change number of rows in matrix

    def changeMatrixName(self, newName: str):

        self.name = str

    # change number of rows in matrix
    def changeNumRows(self, newRows: int):

        self.rows = newRows

     # change number of columns in matrix
    def changeNumCol(self, newCol: int):

        self.columns = newCol




