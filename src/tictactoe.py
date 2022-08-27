"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countActions = 0
    for i in board:
        for j in i:
            if j != EMPTY:
                countActions += 1

    if(countActions % 2 == 0):
        return X
    else:
        return O


def actions(board):
    setOfActions = set()
    for row, i in enumerate(board):
        for cell, j in enumerate(i):
            if j == EMPTY:
                setOfActions.add(tuple((row, cell)))

    return setOfActions


def result(board, action):
    currentBoard = copy.deepcopy(board)
    if(currentBoard[action[0]][action[1]] == EMPTY):
        currentBoard[action[0]][action[1]] = player(currentBoard)
        return currentBoard
    else:
        raise Exception("Invalid action")


def winner(board):
    # Checking Horizontally
    if((board[0][0] == board[0][1] == board[0][2]) and board[0][0] != EMPTY):
        return board[0][0]

    if((board[1][0] == board[1][1] == board[1][2]) and board[1][0] != EMPTY):
        return board[1][0]

    if((board[2][0] == board[2][1] == board[2][2]) and board[2][0] != EMPTY):
        return board[2][0]

    # Checking Vertically
    if((board[0][0] == board[1][0] == board[2][0]) and board[0][0] != EMPTY):
        return board[0][0]
    if((board[0][1] == board[1][1] == board[2][1]) and board[0][1] != EMPTY):
        return board[0][1]
    if((board[0][2] == board[1][2] == board[2][2]) and board[0][2] != EMPTY):
        return board[0][2]

    # Checkign Diagonally
    if((board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY):
        return board[0][0]
    if((board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY):
        return board[0][2]

    return None


def terminal(board):
    # If there is a winner the the game is terminal
    if(winner(board) != None):
        return True

    # If there is no winner and the board has empty space then the game is not terminal
    for i in board:
        for j in i:
            if(j == EMPTY):
                return False

    # Else the game is tie and therefore terminal
    return True


def utility(board):
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    root = GameNode(board)
    root.setMinMaxValue()

    if(player(board) == X):
        return root.getMaxNode().move
    else:
        return root.getMinNode().move


class GameNode:
    def __init__(self, board):
        self.board = board
        self.minMaxValue = None
        self.children = []
        self.move = tuple()

        if(terminal(self.board)):
            self.minMaxValue = utility(self.board)
        else:
            for action in actions(board):
                self.children.append(GameNode(result(board, action)))
                self.children[len(self.children)-1].move = action

    def setMinMaxValue(node):
        listOfMinMax = [child.minMaxValue for child in node.children]
        if(None in listOfMinMax):
            for child in node.children:
                if(terminal(child.board) == False):
                    child.setMinMaxValue()

        listOfMinMax = [child.minMaxValue for child in node.children]
        if(player(node.board) == X):
            node.minMaxValue = max(listOfMinMax)
        else:
            node.minMaxValue = min(listOfMinMax)

    def getMaxNode(node):
        listOfMinMax = [child.minMaxValue for child in node.children]
        indexOfOptimalNode = listOfMinMax.index(max(listOfMinMax))

        return node.children[indexOfOptimalNode]

    def getMinNode(node):
        listOfMinMax = [child.minMaxValue for child in node.children]
        indexOfOptimalNode = listOfMinMax.index(min(listOfMinMax))

        return node.children[indexOfOptimalNode]
