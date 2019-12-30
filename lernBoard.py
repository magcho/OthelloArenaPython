import OthelloLogic
from pprint import pprint

from copy import deepcopy

# user lib
import util
import stackutil


def lern(board):
    """

    Args:
       board arg1

    Returns:


    """

    # board = [
    #     [1, 1, 1, 1, 1, 1, 1, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1, -1],
    #     [1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 0],
    # ]

    board = [
        [0, 1, 0, -1],
        [1, 1, -1, 1],
        [1, -1, 1, 1],
        [-1, 0, -1, 1],
    ]
    boardSize = len(board)

    moves = OthelloLogic.getMoves(board, 1, boardSize)
    maxSocre = 0
    maxSocreMove = moves[0]
    results = []

    # パスの時
    if len(moves) == 0:
        return False

    for move in moves:
        nextBoard = deepcopy(board)
        OthelloLogic.execute(nextBoard, move, 1, boardSize)

        score = evalutionTree(deepcopy(nextBoard), 1, boardSize)
        results.append(score)
        if score > maxSocre:
            score = maxSocre
            maxSocreMove = move

    return maxSocreMove


def evalutionTree(board, player, boardSize):
    """
    
    Returns:
        

    """
    board = OthelloLogic.getReverseboard(board)
    moves = OthelloLogic.getMoves(board, player, boardSize)

    scores = []
    for move in moves:
        nextBoard = deepcopy(board)
        OthelloLogic.execute(nextBoard, move, player * -1, boardSize)

        if util.isGameEnd(nextBoard):
            pprint(nextBoard)
            scores.append(util.getBoardScore(nextBoard))
        else:
            evalutionTree(nextBoard, player * -1, boardSize)

    return 0


lern(None)
# board = [
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, -1],
#     [1, 1, 1, 1, 1, 1, 1, -1],
#     [1, 1, 1, 1, 1, 1, 1, -1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
# ]

# print(util.getBoardHash(board))
# OthelloLogic.printBoard(board)
# print(util.isGameEnd(board))
