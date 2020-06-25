from src.P2.board import *

def collision(board, col, pos):
    for i in range(col):
        if board.queenPos[i] == str(pos) or board.queenPos[col-i-1] == str(pos-i) or board.queenPos[col - i - 1] == str(pos + i):
            return False
    return True

def backtrackingSearch(board, column):
    if column > 8:
        return board
    for pos in range(1,9):
        if collision(board, column, pos):
            board.move(column, pos)
            print(board.queenPos)
            result = backtrackingSearch(board, column + 1)
            if result is not False:
                return result
            board.move(column, 0)
    return False

a = backtrackingSearch(Board(),1)
print()
a.printBoard()