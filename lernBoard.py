import OthelloLogic
from pprint import pprint
import pdb
from copy import deepcopy

# user lib
import util


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

    boardSize = len(board)

    moves = OthelloLogic.getMoves(board, 1, boardSize)
    maxSocre = 0
    maxSocreMove = moves[0]
    results = []

    # 自分がパスで相手は打てる時
    if len(moves) == 0:
        if util.isGameEnd(deepcopy(board)):
            return False

    for move in moves:
        nextBoard = deepcopy(board)
        # util.printMoves(deepcopy(nextBoard), moves, move)
        OthelloLogic.execute(nextBoard, move, 1, boardSize)
        # print("execute root")
        # OthelloLogic.printBoard(deepcopy(nextBoard))
        score = evalutionTree(deepcopy(nextBoard), -1, boardSize)
        results.append(score)
        if score > maxSocre:
            score = maxSocre
            maxSocreMove = move

    return maxSocreMove


def evalutionTree(board, player, boardSize, currentDepth=1):
    # print("evalutionTree")
    # board = OthelloLogic.getReverseboard(board)
    moves = OthelloLogic.getMoves(board, player, boardSize)
    # pprint(board)

    scores = []
    for move in moves:
        # util.printMoves(deepcopy(board), moves, move)
        nextBoard = deepcopy(board)

        OthelloLogic.execute(nextBoard, move, player, boardSize)
        # print("exec")
        # OthelloLogic.printBoard(deepcopy(nextBoard))

        if util.isGameEnd(nextBoard):
            currentPlayer = 1 if currentDepth % 2 == 1 else -1
            scores.append(util.getBoardScore(deepcopy(nextBoard), currentPlayer))
        else:
            scores.append(
                evalutionTree(nextBoard, player * -1, boardSize, currentDepth + 1)
            )

    pprint(board)
    pprint(moves)
    return util.average(scores)


board = [
    [0, 1, 0, -1],
    [0, 1, -1, 1],
    [0, -1, 1, 1],
    [-1, 0, -1, 1],
]
print(lern(board))
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

# board = [[1, 1, 1, 1], [1, -1, -1, -1], [1, 1, -1, -1], [1, 0, 1, -1]]
# moves = OthelloLogic.getMoves(board, -1, 4)
# pprint(moves)


# pprint(util.isGameEnd(board))
