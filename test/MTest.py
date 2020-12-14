import unittest
from model.Cell import Cell
from model.Matrix import Matrix

class TestState(unittest.TestCase):
    #place avatar
    # - errors: Avatar is being placed on already occupied tile
    #           Avatars are being placed on empty tile
    # - behavior: Test if map is populated with designated coordinate given by place_penguin function

    def test_place_avatar(self):

        m1 = Matrix("m1", 2, 2, 0, 0)
        m3 = Matrix("m3", 2, 2, 0, 0)
        c1 = Cell(0, 0, 0, 0, 0, 0)
        print(m1)

        cellLis = [c1, c1]
        finalLis = [cellLis, cellLis]

        m1.makeMatrix()
        m3.makeMatrix()



    # Test to make sure error is thrown to place avatar on occupied tile
    def test_place_wrong_avatar_tile(self):
        m2 = Matrix("m2", 2, 2, 0, 0)
        print(m2)
        m2.makeMatrix()
        m2.initiateProbs()

        cell1 = m2.getL2()[0][0]

        self.assertEqual(cell1.getProb(), 0.25)



    
