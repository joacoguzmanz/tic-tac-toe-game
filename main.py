from functions import *

print('\nWelcome to the Tic Tac Toe!\n')

while True:

    board = [' '] * 10
    playerOneMarker, playerTwoMarker = playerInput()
    turn = chooseFirstPlayer()
    print(f'{turn} goes first')

    gameStart = input('Ready to start playing? (Y or N) ')

    if gameStart.lower() == 'y':
        gameReady = True
    else:
        gameReady = False

    while gameReady:
        if turn == 'Player 1':
            displayBoard(board)
            nextPosition = playerPositionChoice(board)
            placeMarker(board, playerOneMarker, nextPosition)

            if winCheck(board, playerOneMarker):
                displayBoard(board)
                print('Congratulations! Player one has won!')
                gameReady = False
            else:
                if isBoardFull(board):
                    displayBoard(board)
                    print('It\'s a draw! ')
                    break
                else:
                    turn = 'Player 2'
        else:
            displayBoard(board)
            nextPosition = playerPositionChoice(board)
            placeMarker(board, playerTwoMarker, nextPosition)

            if winCheck(board, playerTwoMarker):
                displayBoard(board)
                print('Player two has won, congratulations!')
                gameReady = False
            else:
                if isBoardFull(board):
                    displayBoard(board)
                    print('It\'s a draw! ')
                    break
                else:
                    turn = 'Player 1'

    if playAgain():
        continue
    else:
        break    

print('\nThanks for playing!\n')