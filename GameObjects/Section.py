

class Section:
    """ Section class

    This class handles a section of a sudoku board
    """

    def __init__(self):
        """ Init function of the section class

        self - the instance itself
        """
        self.fields = {
            'a': [0, 0, 0],
            'b': [0, 0, 0],
            'c': [0, 0, 0]
        }

    """ Get the field value

    self - the instance itself
    coordinates - a list with the coordinates
    """
    def get_field(self, coordinates):
        if coordinates[0] in self.fields:
            raise Exception('The coordinates are invalid')
        if coordinates[1] in [1, 2, 3]:
            raise Exception('The coordinates are invalid')

        return self.fields[coordinates[0]][coordinates[1]]
