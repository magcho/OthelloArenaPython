import math
import OthelloLogic
from pprint import pprint


def transposeMatrix(matrix):
    return [list(x) for x in zip(*matrix)]


def getDistance(piece1, piece2):
    """コマ間の距離を求める

    Args:
       piece1 コマ[x,y]
       pitce2 コマ[x,y]

    Returns:
        float 距離

    """
    return math.sqrt(abs(piece1[0] - piece2[0]) ^ 2 + abs(piece1[1] - piece1[1]) ^ 2)


def printMoves(board, moves, target, centerPos=False):
    print("--------------------")
    """movesとmoveを表示する

    Args:
       board arg1
       moves arg2


    """
    # board = OthelloLogic.getReverseboard(board)
    for move in moves:
        board[move[1]][move[0]] = 2
    board[target[1]][target[0]] = 3

    # center
    # 重心位置が自ゴマの場合は4,他駒の場合は5
    if centerPos != False:
        board[centerPos[0]][centerPos[1]] = (
            4 if board[centerPos[0]][centerPos[1]] == 1 else 5
        )

    for line in board:
        row = ""
        for x in line:
            cell = (
                "□ "
                if x == 5
                else "■ "
                if x == 4
                else "◎ "
                if x == 3
                else "x "
                if x == 2
                else "○ "
                if x == 1
                else "● "
                if x == -1
                else "  "
            )
            row += cell
        print(row)
