import unittest
from model.Cell import Cell
from model.Matrix import Matrix

class MatrixTest(unittest.TestCase):

# (self, P1Strat: int, P2Strat: int, Weight: int, Probability: float,
# Min: float, Max: float)

# (self, name: str, columns: int, rows: int, epsilon: float, delta: float)
    def test_initialize(self):

        m1 = Matrix("m1", 2, 2, 0, 0, [],[5, 3], [5, 3])
        print(m1)


        m1.makeMatrix()


    #works
    def test_probabilities(self):

        m2 = Matrix("m2", 2, 2, 1, 0.99, [],[5, 3], [5, 3])
        m2.makeMatrix()
        m2.initiateProbs()

        cell1 = m2.getL2()[0][0]

        self.assertEqual(cell1.getProb(), 0.25)

