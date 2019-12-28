import random
from pprint import pprint

# user lib
import util


def action(board, moves, size=8):
    # 撃てる場所が1つしかない場合はそこに打つ
    if len(moves) == 1:
        return moves[0]

    centerPos = getCenter(board)
    print("centerPos:", centerPos)

    minDistance = 100
    minDistanceIndex = 0
    returnMove = moves[0]
    for move in moves:
        distance = util.getDistance(move, centerPos)
        if ignoreSideLine(board, moves, move):
            print("ignore")
            continue
        if distance < minDistance:
            minDistance = distance
            returnMove = move

    util.printMoves(board, moves, returnMove, centerPos)
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


def ignoreSideLine(board, moves, target):
    """盤の一番外側の列は有効てであることが多いので避ける

    Args:
       board 盤
       moves 
       move 

    Returns:
        bool

    """
    # sideではない場合はスキップしない
    boardSize = len(board)
    if (
        target[0] != 0
        or target[0] != boardSize
        or target[1] != 0
        or target[1] != boardSize
    ):
        return False

    # movesの全てが外側の列であることがあるのでその場合はスキップしない
    count = 0
    sideFlag = False
    for move in moves:
        if (move[0] == 0 and move[0] == (boardSize - 1)) or (
            move[1] == 0 and move[1] == (boardSize - 1)
        ):
            sideFlag = True
            count = count + 1

    # 全てがsideのケース
    if sideFlag and count == len(moves):
        print("全てがside")
        return False

    # side以外もある場合
    print("side以外もある")
    return True
