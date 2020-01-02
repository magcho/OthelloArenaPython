import OthelloLogic
from pprint import pprint

# import pdb
from copy import deepcopy

import sys

# import os

from concurrent.futures import ProcessPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger

# from multiprocessing import Pool
# import threading

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


def lern(board, moves):
    """

    Args:
       board arg1

    Returns:


    """
    # init_logger()

    boardSize = len(board)

    # moves = OthelloLogic.getMoves(board, 1, boardSize)
    minScore = boardSize ** 2
    minScoreMove = moves[0]
    maxScore = 0
    maxScoreMove = moves[0]

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
    # pprint(params)

    results = []

    # TYPE 9 78.072
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(evalFunc, params))

    # TYPe 8 76.085
    # with ProcessPoolExecutor(max_workers=8) as executor:
    #     results = list(executor.map(evalFunc, params))

    # TYPE 7 80.120
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     results = list(executor.map(evalFunc, params))

    # TYPE 6 77.393
    # with ProcessPoolExecutor(max_workers=8) as executor:
    #     for result in executor.map(evalFunc, params):
    #         results.append(result)

    # TYPE5 79.082
    # (max_workers, chunk_sizs, num_tasks, num_calc) = (2, 100, 10000, 1000)
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     for result in executor.map(evalFunc, params):
    #         results.append(result)

    # TYPE0 189.294
    # for param in params:
    #     results.append(evalFunc(param))

    # TYPE4 199.272
    # threads = []
    # for param in params:
    #     thread = MyThread(param)
    #     thread.start()
    #     threads.append(thread)
    # for th in threads:
    #     th.join()
    # for r in threads:
    #     results.append(r.getResult())

    # TYPE3 188.869
    # (max_workers, chunk_sizs, num_tasks, num_calc) = (2, 100, 10000, 1000)
    # with ProcessPoolExecutor(max_workers=max_workers) as executor:
    #     for result in executor.map(evalFunc, params, chunksize=chunk_sizs):
    #         results.append(result)

    # TYPE2 80.166
    # with Pool(processes=4) as pool:
    #     results = pool.map(evalFunc, params)

    # TYPE1 78.372
    # pool = Pool(processes=4)
    # results = pool.map(evalFunc, params)
    # pool.close()
    # pool.join()

    # pprint(results)

    # min
    for i in range(len(results)):
        if results[i] <= minScore:
            minScore = results[i]
            minScoreMove = moves[i]

    # max
    # for i in range(len(results) - 1):
    # if results[i] > maxScore:
    # maxScore = results[i]
    # maxScoreMove = moves[i]

    pprint(results)
    print(minScore)
    pprint(moves)
    return minScoreMove


# class MyThread(threading.Thread):
#     def __init__(self, param):
#         super().__init__()
#         (self.board, self.move, self.boardSize) = param

#     def run(self):
#         OthelloLogic.execute(self.board, self.move, 1, self.boardSize)
#         self.result = evalutionTree(deepcopy(self.board), -1, self.boardSize)

#     def getResult(self):
#         return self.result


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
            # getLogger().info(currentDepth)
            # getLogger().info("I am {}, pid {}".format(currentDepth, os.getpid()))
        else:
            scores.append(
                evalutionTree(nextBoard, player * -1, boardSize, currentDepth + 1)
            )
    return min(scores)


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
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, -1, -1, -1, -1, -1, -1, 1],
#     [0, -1, -1, -1, 1, 1, -1, 1],
#     [1, -1, -1, 1, 1, 1, -1, 1],
#     [0, -1, -1, -1, 1, 1, -1, 1],
#     [0, 0, -1, -1, 1, 1, -1, 1],
#     [0, 0, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
# ]
# print(lern(board))

# print(util.getBoardHash(board))
# OthelloLogic.printBoard(board)
# print(util.isGameEnd(board))

# board = [[1, 1, 1, 1], [1, -1, -1, -1], [1, 1, -1, -1], [1, 0, 1, -1]]
# moves = OthelloLogic.getMoves(board, -1, 4)
# pprint(moves)


# pprint(util.isGameEnd(board))
