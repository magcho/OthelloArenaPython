import OthelloLogic
import lernBoard
import util
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

    if lastPieceCount > 8:
        return center.action(board, moves)

    else:
        return lernBoard.lern(board, moves)
