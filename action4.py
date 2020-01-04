import OthelloLogic
from pprint import pprint
import lernBoard
import util
import action1
import center
import time


def action(board, moves):
    """

    Args:
       board arg1
       moves arg2

    Returns:
        move

    """
    lastPieceCount = (len(board) ** 2) - util.getOnBoardPieces(board)

    if lastPieceCount > 8:
        return center.action(board, moves)
        # return action1.action(board, moves)
    else:
        return lernBoard.lern(board, moves)

    # if util.getOnBoardPieces(board) > (len(board) ** 2) - 12:
    #     return lernBoard.lern(board, moves)
    # else:
    #     print("start full search")
    #     return action1.action(board, moves)


# board = [
#     [0, 1, 1, 1, 1, 1, 1, 0],
#     [-1, -1, -1, -1, -1, -1, -1, 0],
#     [1, 1, 1, -1, 1, -1, 0, 1],
#     [1, 1, -1, 1, -1, -1, -1, 1],
#     [1, 1, -1, -1, 1, -1, 0, 1],
#     [-1, -1, -1, -1, 1, -1, 0, 0],
#     [-1, -1, -1, -1, -1, -1, 0, 0],
#     [0, -1, -1, -1, -1, -1, -1, 0],
# ]
# OthelloLogic.printBoard(board)
# moves = OthelloLogic.getMoves(board, 1, 8)
# start = time.time()
# print(lernBoard.lern(board, moves))
# stop = time.time()
# print("%.3f seconds" % (stop - start))