import OthelloLogic
from pprint import pprint
from copy import deepcopy
import sys
from concurrent.futures import ProcessPoolExecutor

# 再帰呼び出し上限
sys.setrecursionlimit(10000)

# user lib
import util


def lern(board, moves):
    """

    Args:
       board arg1

    Returns:


    """
    boardSize = len(board)
    minScore = boardSize ** 2
    minScoreMove = moves[0]

    # 最終手の場合探索を行わない
    if util.getOnBoardPieces(board) == (boardSize ** 2) - 1:
        moves = OthelloLogic.getMoves(board, 1, boardSize)
        return moves[0]

    # 自分がパスで相手は打てる時
    if len(moves) == 1:
        return moves[0]
    if len(moves) == 0:
        if util.isGameEnd(deepcopy(board)):
            return moves[0]

    params = []
    for move in moves:
        params.append((deepcopy(board), move, boardSize))

    results = []
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(evalFunc, params))

    # min
    for i in range(len(results)):
        if results[i] <= minScore:
            minScore = results[i]
            minScoreMove = moves[i]

    pprint(results)
    pprint(moves)
    return minScoreMove


def evalFunc(params):
    (board, move, boardSize) = params

    OthelloLogic.execute(board, move, 1, boardSize)
    return evalutionTree(board, -1, boardSize)


def evalutionTree(board, player, boardSize, currentDepth=1):
    moves = OthelloLogic.getMoves(board, player, boardSize)

    # パスの時
    if moves == []:
        return evalutionTree(deepcopy(board), player * -1, boardSize)

    scores = []
    for move in moves:
        nextBoard = deepcopy(board)
        OthelloLogic.execute(nextBoard, move, player, boardSize)

        if util.isGameEnd(nextBoard):
            currentPlayer = 1 if currentDepth % 2 == 1 else -1
            scores.append(util.getBoardScore(deepcopy(nextBoard), currentPlayer))
        else:
            scores.append(
                evalutionTree(nextBoard, player * -1, boardSize, currentDepth + 1)
            )
    return min(scores)
