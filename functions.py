from random import randint

def clearOutput():
    print('\n'*100)


def displayBoard(board):
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')


def playerInput():
    playersMarkers = {
        'player1': ' ',
        'player2': ' '
    }

    marker = input('What marker do you want to use? (X or O) ')

    while not (marker.lower() == 'x' or marker.lower() == 'o'):
        print('Not X nor O!')
        marker = input('What marker do you want to use? (X or O) ')

    playersMarkers.update({'player1': marker.upper()})

    if playersMarkers['player1'] == 'X':
        playersMarkers.update({'player2': 'O'})

    if playersMarkers['player1'] == 'O':
        playersMarkers.update({'player2': 'X'})

    return playersMarkers.values()


def placeMarker(board, marker, position):
    board[position] = marker


def winCheck(board, mark):
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or 
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)): 
        return True
    else:
        return False


def chooseFirstPlayer():
    firstPlayer = randint(1, 2)

    if firstPlayer == 1:
        return 'Player 1'
    elif firstPlayer == 2:
        return 'Player 2'


def checkSpace(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def isBoardFull(board):
    for i in range(1, 10):
        if checkSpace(board, i):
            return False
    return True


# Add check to see if input is a number
def playerPositionChoice(board):
    nextPosition = 0

    while nextPosition not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not checkSpace(board, nextPosition):
        nextPosition = int(input('Choose your next position: [1 - 9] '))

    return nextPosition


def playAgain():
    play = input('Do you want to play again? (Y or N): ')

    while not (play.lower() == 'y' or play.lower() == 'n'):
        play = input('Do you want to play again? (Y or N): ')

    if play.lower() == 'y':
        return True

    if play.lower() == 'n':
        return False
