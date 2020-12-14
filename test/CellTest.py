import unittest
from model.Cell import Cell

class CellTest(unittest.TestCase):

#(self, P1Strat: int, P2Strat: int Probability: float, Min: float, Max: float)
    def test_getters(self):

        c1 = Cell(5, 5, 1, 0, 0)

        self.assertEqual(c1.getP1Strat(), 5)
        self.assertEqual(c1.getP2Strat(), 5)
        self.assertEqual(c1.getProb(), 1)
        self.assertEqual(c1.getMin(), 0)
        self.assertEqual(c1.getMax(), 0)


    def test_setters(self):

        c1 = Cell(5, 5, 1, 0, 0)

        c1.setP1Strat(2)
        c1.setP2Strat(2)
        c1.setProb(0.5)
        c1.setMax(0.1)
        c1.setMin(0.01)


        self.assertEqual(c1.getP1Strat(), 2)
        self.assertEqual(c1.getP2Strat(), 2)
        self.assertEqual(c1.getProb(), 0.5)
        self.assertEqual(c1.getMax(), 0.1)
        self.assertEqual(c1.getMin(), 0.01)




if __name__ == '__main__':
    unittest.main()



