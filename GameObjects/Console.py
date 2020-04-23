import os
import sys


class Console:
    """Class for handling the console output.

    This class is a wrapper for the console output
    it is used to provide clear functions for certain
    commands such as the clear command
    """

    def __init__(self):
        self.output = ''
        self.board = None
        self.printTitle()

    @staticmethod
    def newLine():
        """Returns a new line character."""
        return '\n'

    def printTitle(self):
        """Print the title of the game.

        self - The instance of the console
        """
        self.output += 'Sudoku' + Console.newLine()
        self.output += 'Copyright Kevin Ditscheid <kevin@the-coding-owl.de>' + Console.newLine()
        self.output += Console.newLine()
        self.output += Console.newLine()

    def printGameMenu(self):
        """Print the game menu.

        self - The instance of the console
        """
        self.output += 'Game Menu' + Console.newLine()
        self.output += '1) New Game' + Console.newLine()
        self.output += '2) Load Game' + Console.newLine()
        self.output += '3) Save Game' + Console.newLine()
        self.output += 'e) Exit' + Console.newLine()
        self.output += Console.newLine()
        self.dump()
        return input('Please choose:')

    def printStartNewGame(self):
        """Print the new game message

        self - The instance of the console
        """
        self.output += 'Starting new game' + Console.newLine()

    def printSaveGameMenu(self, files):
        """Print the save game menu

        self - The instance of the console
        files - The list of existing savegames
        """
        self.output += 'Existing saves' + Console.newLine()
        for file in files:
            self.output += ': ' + file + Console.newLine()
        self.output += Console.newLine()
        self.dump()
        return input('Enter the save name:(enter "q" to abbort)' + Console.newLine())

    def askOverride(self, filename):
        """Ask if the file should get overridden

        self - The instance of the console
        filename - The filename to be overridden
        """
        override = input('Should the save state "' + filename + '" be overridden?(y|n)' + Console.newLine())
        if override == 'y':
            return True
        else:
            return False

    def printSaved(self):
        """Print the game saved message"""
        self.output += 'Game saved successfully' + Console.newLine()

    def clear(self):
        """Clear the console.

        self - The instance of the console
        """
        self.output = ''
        self.printTitle()

    def printError(self, message):
        """Print an error message.

        self - The instance of the console
        message - The message to be printed
        """
        self.output += message + Console.newLine()

    def printBoard(self):
        """Print the board

        self - The instance of the console
        """
        self.output += '+-----+-----+-----+-----+-----+-----+-----+-----+-----+' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('a', '1') + '     ' + self.board.getCoordinate('a', '2') + '     ' + self.board.getCoordinate('a', '3') + '  |  ' + self.board.getCoordinate('a', '4') + '     ' + self.board.getCoordinate('a', '5') + '     ' + self.board.getCoordinate('a', '6') + '  |  ' + self.board.getCoordinate('a', '7') + '     ' + self.board.getCoordinate('a', '8') + '     ' + self.board.getCoordinate('a', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('b', '1') + '     ' + self.board.getCoordinate('b', '2') + '     ' + self.board.getCoordinate('b', '3') + '  |  ' + self.board.getCoordinate('b', '4') + '     ' + self.board.getCoordinate('b', '5') + '     ' + self.board.getCoordinate('b', '6') + '  |  ' + self.board.getCoordinate('b', '7') + '     ' + self.board.getCoordinate('b', '8') + '     ' + self.board.getCoordinate('b', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('c', '1') + '     ' + self.board.getCoordinate('c', '2') + '     ' + self.board.getCoordinate('c', '3') + '  |  ' + self.board.getCoordinate('c', '4') + '     ' + self.board.getCoordinate('c', '5') + '     ' + self.board.getCoordinate('c', '6') + '  |  ' + self.board.getCoordinate('c', '7') + '     ' + self.board.getCoordinate('c', '8') + '     ' + self.board.getCoordinate('c', '9') + '  |' + Console.newLine()
        self.output += '+-----+-----+-----+-----+-----+-----+-----+-----+-----+' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('d', '1') + '     ' + self.board.getCoordinate('d', '2') + '     ' + self.board.getCoordinate('d', '3') + '  |  ' + self.board.getCoordinate('d', '4') + '     ' + self.board.getCoordinate('d', '5') + '     ' + self.board.getCoordinate('d', '6') + '  |  ' + self.board.getCoordinate('d', '7') + '     ' + self.board.getCoordinate('d', '8') + '     ' + self.board.getCoordinate('d', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('e', '1') + '     ' + self.board.getCoordinate('e', '2') + '     ' + self.board.getCoordinate('e', '3') + '  |  ' + self.board.getCoordinate('e', '4') + '     ' + self.board.getCoordinate('e', '5') + '     ' + self.board.getCoordinate('e', '6') + '  |  ' + self.board.getCoordinate('e', '7') + '     ' + self.board.getCoordinate('e', '8') + '     ' + self.board.getCoordinate('e', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('f', '1') + '     ' + self.board.getCoordinate('f', '2') + '     ' + self.board.getCoordinate('f', '3') + '  |  ' + self.board.getCoordinate('f', '4') + '     ' + self.board.getCoordinate('f', '5') + '     ' + self.board.getCoordinate('f', '6') + '  |  ' + self.board.getCoordinate('f', '7') + '     ' + self.board.getCoordinate('f', '8') + '     ' + self.board.getCoordinate('f', '9') + '  |' + Console.newLine()
        self.output += '+-----+-----+-----+-----+-----+-----+-----+-----+-----+' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('g', '1') + '     ' + self.board.getCoordinate('g', '2') + '     ' + self.board.getCoordinate('g', '3') + '  |  ' + self.board.getCoordinate('g', '4') + '     ' + self.board.getCoordinate('g', '5') + '     ' + self.board.getCoordinate('g', '6') + '  |  ' + self.board.getCoordinate('g', '7') + '     ' + self.board.getCoordinate('g', '8') + '     ' + self.board.getCoordinate('g', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('h', '1') + '     ' + self.board.getCoordinate('h', '2') + '     ' + self.board.getCoordinate('h', '3') + '  |  ' + self.board.getCoordinate('h', '4') + '     ' + self.board.getCoordinate('h', '5') + '     ' + self.board.getCoordinate('h', '6') + '  |  ' + self.board.getCoordinate('h', '7') + '     ' + self.board.getCoordinate('h', '8') + '     ' + self.board.getCoordinate('h', '9') + '  |' + Console.newLine()
        self.output += '|  ' + self.board.getCoordinate('i', '1') + '     ' + self.board.getCoordinate('i', '2') + '     ' + self.board.getCoordinate('i', '3') + '  |  ' + self.board.getCoordinate('i', '4') + '     ' + self.board.getCoordinate('i', '5') + '     ' + self.board.getCoordinate('i', '6') + '  |  ' + self.board.getCoordinate('i', '7') + '     ' + self.board.getCoordinate('i', '8') + '     ' + self.board.getCoordinate('i', '9') + '  |' + Console.newLine()
        self.output += '+-----+-----+-----+-----+-----+-----+-----+-----+-----+' + Console.newLine()

    def dump(self):
        """Dump the output buffer to console

        self - The instance of the console
        """
        if sys.platform.startswith('linux'):
            os.system('clear')
        else:
            os.system('cls')
        print(self.output)

    def setBoard(self, board):
        """Set the board

        self - The instance of the console
        board - The board to set
        """
        self.board = board

    @staticmethod
    def exit():
        """Exit the program."""
        print('Exiting!')
        exit(0)
