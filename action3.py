import OthelloLogic
from pprint import pprint
import lernBoard
import util
import action1


def action(board, moves):
    """

    Args:
       board arg1
       moves arg2

    Returns:
        move

    """

    # return lernBoard.lern(board)
    if util.getOnBoardPieces(board) > (len(board) ** 2) - 16:
        return lernBoard.lern(board)

    else:
        return action1.action(board, moves)
