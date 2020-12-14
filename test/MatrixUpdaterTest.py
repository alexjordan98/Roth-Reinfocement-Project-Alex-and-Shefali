import unittest
from model.Cell import Cell
from model.Matrix import Matrix
from model.MatrixUpdater import MatrixUpdater

class MatrixUpdaterTest(unittest.TestCase):


#def __init__(self, startState: Matrix, iterations: int, totalWeight: int):


    def test_initialize(self):

        0==0
        #m2 = Matrix("m2", 10, 10, 0, 0)
        #m2.makeMatrix()
        #m2.initiateProbs()

        #updater = MatrixUpdater(m2, 10, 0)

        #updater.setCellRange(m2)

    def test_makestates(self):

        #l1 = [1,1,1,1,1,1,1,1,1,1]
        #l2 = [1,1,1,1,1,1,1,1,1,1]


        #m3 = Matrix("m0", 10, 10, 0, 0.99, [],l1, l2)

        #m3.makeMatrix()

        #updater2 = MatrixUpdater(10, [])
        0==0
        #updater2.makeStates(m3)


    def test_itter(self):


        l1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        l2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        m4 = Matrix("m0", 10, 10, 0.5, 0.01, [], l1, l2)
        m4.makeMatrix()

        updater3 = MatrixUpdater(10, [])

        updater3.itter(m4)