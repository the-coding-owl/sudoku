import GameObjects.Console
import GameObjects.Board
import GameObjects.FileHandler

console = GameObjects.Console.Console()
board = GameObjects.Board.Board()
fileHandler = GameObjects.FileHandler.FileHandler()

while True:
    console.clear()
    selection = console.printGameMenu()

    if selection == 'e':
        # Exit the game
        console.exit()
    elif selection == '1':
        while True:
            console.clear()
            console.printBoard()
            play = console.printBoardMenu()
            if play == 'm':
                break
            else:
                board.setCoordinates(play)
    elif selection == '1':
        # Generate new sudoku board
        console.printStartNewGame()
        board.new()
        console.setBoard(board)
        console.printBoard()
    elif selection == '2':
        # Load existing save file
        files = fileHandler.readSavegames()
        while True:
            console.clear()
            load = console.printLoadGameMenu(files)
            board.load(fileHandler.read(files[load - 1]))
            break
    elif selection == '3':
        # Save game
        files = fileHandler.readSavegames()
        while True:
            console.clear()
            filename = console.printSaveGameMenu(files)
            if filename == 'q':
                break
            check = fileHandler.checkFile(filename)
            if check == 'override':
                override = console.askOverride(filename)
                if override:
                    fileHandler.override(filename, board)
                else:
                    break
            elif check == 'new':
                fileHandler.create(filename, board)
                console.printSaved()
                break
            else:
                console.printError('Wront Input!')
                break
    else:
        # made a wrong input
        console.printError('Wrong input!')
    console.dump()
