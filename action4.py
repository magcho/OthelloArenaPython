import OthelloLogic
from pprint import pprint
import lernBoard
import util
import action1
import center


def action(board, moves):
    """

    Args:
       board arg1
       moves arg2

    Returns:
        move

    """
    lastPieceCount = (len(board) ** 2) - util.getOnBoardPieces(board)

    if lastPieceCount > 12:
        return center.action(board, moves)
        # return action1.action(board, moves)
    else:
        return lernBoard.lern(board, moves)

    if util.getOnBoardPieces(board) > (len(board) ** 2) - 12:
        return lernBoard.lern(board, moves)
    else:
        print("start full search")
        return action1.action(board, moves)
