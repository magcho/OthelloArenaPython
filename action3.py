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

    if util.getOnBoardPieces(board) > (len(board) ** 2) - 12:
        return lernBoard.lern(board, moves)

    else:
        return action1.action(board, moves)
