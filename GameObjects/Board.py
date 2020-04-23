"""" The board class that handles the sudoku grid

This class handles the sudoku grid.
"""

import random
import GameObjects.Section


class Board:

    """ Init function of the Sudoku class

    self - the instance itself
    """
    def __init___(self):
        self.sections = []
        self.isGenerated = False

    """ Generate a new sudoku board

    self - the instance itself
    """
    def new(self):
        # fill board
        for i in xrange(0, 9):
            for k in xrange('a', 'j'):
                randInt = random.randint(1, 9)
                self.board = randInt;
        self.isGenerated = True

    def getCoordinate