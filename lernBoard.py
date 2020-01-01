import OthelloLogic
from pprint import pprint
import pdb
from copy import deepcopy
import sys

# 再帰呼び出し上限
sys.setrecursionlimit(10000)

# user lib
import util


def lern(board):
    """

    Args:
       board arg1

    Returns:


    """

    boardSize = len(board)

    moves = OthelloLogic.getMoves(board, 1, boardSize)
    minScore = boardSize ** 2
    minScoreMove = moves[0]

    # 最終手の場合探索を行わない
    if util.getOnBoardPieces(board) == (boardSize ** 2) - 1:
        moves = OthelloLogic.getMoves(board, 1, boardSize)
        return moves[0]

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
        if score < minScore:
            score = minScore
            minScoreeMove = move
    print(minScore)
    return minScoreMove


def evalutionTree(board, player, boardSize, currentDepth=1):
    # print("evalutionTree")
    # board = OthelloLogic.getReverseboard(board)
    moves = OthelloLogic.getMoves(board, player, boardSize)
    # pprint(board)

    # パスの時
    if moves == []:
        return evalutionTree(deepcopy(board), player * -1, boardSize)

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
    return util.average(scores)


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
