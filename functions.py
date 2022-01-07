from random import randint
from typing import NewType


def clearOutput():
    print('\n'*100)


def displayBoard(board):
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')


def playerInput():
    playersMarkers = {
        'player1': ' ',
        'player2': ' '
    }

    marker = input('What marker do you want to use? (X or O) ')

    while not (marker.lower() == 'x' or marker.lower() == 'o'):
        print('Not X nor O!')
        marker = input('What marker do you want to use? (X or O)')

    playersMarkers.update({'player1': marker.upper()})

    if playersMarkers['player1'] == 'X':
        playersMarkers.update({'player2': 'O'})

    if playersMarkers['player1'] == 'O':
        playersMarkers.update({'player2': 'X'})

    return playersMarkers.items()


def placeMarker(board, marker, position):
    board.pop(position)
    board.insert(position, marker)


def winCheck(board, mark):
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or  # first row
            # second row
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # third row
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # first col
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            # second col
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            # third col
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # first diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)):  # second diagonal
        return True
    else:
        return False


def chooseFirstPlayer():
    firstPlayer = randint(1, 2)

    if firstPlayer == 1:
        return 'Player 1 first'
    elif firstPlayer == 2:
        return 'Player 2 first'


def checkSpace(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def checkFullBoard(board):
    if ' ' not in board:
        return True
    else:
        return False


# Add check to see if input is a number
def playerPositionChoice(board):
    nextPosition = int(input('What is your next position? (1 to 9) '))

    while not (nextPosition >= 1 and nextPosition <= 9):
        nextPosition = int(input('Enter a number between 1 and 9: '))

    if checkSpace(board, nextPosition):
        return nextPosition
    else:
        return -1


def playAgain():
    play = input('Do you want to play again? (Y or N): ')

    while not (play.lower() == 'y' or play.lower() == 'n'):
        play = input('Do you want to play again? (Y or N): ')

    if play.lower() == 'y':
        return True

    if play.lower() == 'n':
        return False
