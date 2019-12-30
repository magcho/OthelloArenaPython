import OthelloLogic
from pprint import pprint
import util


def action(board, moves):
    """

    Args:
       board arg1
       moves arg2

    Returns:
        move

    """

    boardSize = len(board)

    board = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        # [-1, -1, 1, 1, -1, -1, -1, -1],
        # [-1, 1, -1, -1, 1, -1, -1, -1],
        # [-1, 1, -1, -1, -1, 1, -1, -1],
        # [-1, -1, -1, -1, -1, -1, -1, -1],
        # [-1, -1, 1, 1, 1, 1, 1, -1],
        # [-1, -1, -1, 1, 1, -1, -1, 1],
        # [1, 1, 1, 1, 1, 1, -1, 1],
    ]

    print(util.getBoardScore(board))

    return moves[0]
