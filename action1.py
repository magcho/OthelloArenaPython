import random
from pprint import pprint

# user lib
import util


def action(board, moves, size=8):
    centerPos = getCenter(board)

    minDistance = 0
    minDistanceIndex = 0
    returnMove = moves[0]
    # init value
    for move in moves:
        distance = util.getDistance(move, centerPos)
        if distance < minDistance:
            minDistance = distance
            returnMove = move
    return returnMove

    # random
    # index = random.randrange(len(moves))
    # return moves[index]


def getCenter(board):
    """自分の色の駒の重心の座標を返す

    Args:
       board 現在の盤面の状態

    Returns:
        重心の座標(xPos, yPos)

    """
    boardSize = len(board)
    # line center
    lineSum = []
    for line in board:
        lineSum.append(sum([piece for piece in line if piece == 1]))

    tmp = 0
    for i in range(boardSize):
        tmp = tmp + lineSum[i] * (i + 1)
    yCenter = (tmp / sumMyPiece(board)) - 1

    # 転置
    tboard = util.transposeMatrix(board)

    # coloum center
    columnSum = []
    for line in tboard:
        columnSum.append(sum([piece for piece in line if piece == 1]))

    tmp = 0
    for i in range(boardSize):
        tmp = tmp + columnSum[i] * (i + 1)
    xCenter = (tmp / sumMyPiece(board)) - 1

    return [int(xCenter), int(yCenter)]


def sumMyPiece(board):
    """盤に自分の駒が何個あるか

    Args:
       board 現在の盤面の状態

    Returns:
        自分の駒の個数

    """
    myPiece = 0
    for line in board:
        for piece in line:
            if piece == 1:
                myPiece = myPiece + 1
    return myPiece
