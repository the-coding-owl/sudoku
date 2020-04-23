import os


class FileHandler:
    """A wrapper class for file handling"""

    def __init__(self):
        self.workingdir = os.getcwd() + '/savegames'
        if not os.path.exists(self.workingdir):
            os.mkdir(self.workingdir)

    def readSavegames(self):
        """Read the savegames"""
        return os.listdir(self.workingdir)

    def override(self, filename, board):
        """Override the file"""
        self.create(filename, board)

    def create(self, filename, board):
        """Create a new save file"""
        file = open(self.workingdir + '/' + filename, mode='w')
        for i in range('a', 'j'):
            for j in range(1, 10):
                file.write(board.getCoordinate(i, j) + ',')
            file.write('\n')
        file.close()

    def checkFile(self, filename):
        """Check the given filename"""
        if not filename:
            return False
        if os.path.exists(self.workingdir + '/' + filename):
            return 'override'
        else:
            return 'new'
