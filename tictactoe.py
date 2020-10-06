"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    numbers_of_x = 0
    numbers_of_y = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numbers_of_x += 1
            elif board[i][j] == O:
                numbers_of_y += 1

    if numbers_of_x <= numbers_of_y:
        return X

    return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    rev = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                rev.add((i, j))

    return rev
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        return board
    temp = copy.deepcopy(board)
    if action not in actions(temp):
        raise Exception('Invalid action')

    temp[action[0]][action[1]] = player(board)
    return temp
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not None and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] is not None and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] is not None and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] is not None and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    playing = player(board)
    v = -math.inf
    next_action = None

    if playing == X:
        for action in actions(board):
            tmp = min_value(result(board, action))
            if v < tmp:
                v = tmp
                next_action = action
        return next_action

    v = math.inf
    for action in actions(board):
        tmp = max_value(result(board, action))
        if v > tmp:
            v = tmp
            next_action = action
    return next_action

    # raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
