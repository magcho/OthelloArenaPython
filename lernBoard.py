import OthelloLogic
from pprint import pprint
import pdb
from copy import deepcopy
import sys
from concurrent.futures import ProcessPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger

# 再帰呼び出し上限
sys.setrecursionlimit(10000)

# user lib
import util


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def lern(board):
    """

    Args:
       board arg1

    Returns:


    """
    init_logger()

    boardSize = len(board)

    moves = OthelloLogic.getMoves(board, 1, boardSize)
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
    (max_workers, chunk_sizs, num_tasks, num_calc) = (2, 100, 10000, 1000)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for result in executor.map(evalFunc, params, chunksize=chunk_sizs):
            results.append(result)

    pprint(results)
    for i in range(len(results) - 1):
        if results[i] < minScore:
            score = minScore
            minScoreMove = moves[i]

    print(minScore)
    return minScoreMove


def evalFunc(params):
    (board, move, boardSize) = params

    OthelloLogic.execute(board, move, 1, boardSize)
    return evalutionTree(board, -1, boardSize)


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
