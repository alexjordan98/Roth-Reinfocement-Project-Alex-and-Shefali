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



