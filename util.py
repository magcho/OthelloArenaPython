import math
import OthelloLogic
from pprint import pprint
from copy import deepcopy


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


def printMoves(board, moves, target=False, centerPos=False):
    print("--------------------")
    """movesとmoveを表示する

    Args:
       board arg1
       moves arg2


    """
    for move in moves:
        board[move[1]][move[0]] = 2
    if target != False:
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


def getBoardScore(board):
    """完全に埋まったboardの点数を返す。

    Args:
       board 

    Returns:
        点数

    """
    myPieceCount = len([cell for line in board for cell in line if cell == 1])
    return 2 * myPieceCount - len(board) ** 2


def isGameEnd(board):
    """ゲームが終了したかどうか判定する
    
    Args:
       board ${1:arg1}

    Returns:
        bool $0

    """
    boardSize = len(board)
    currentPiece = len([cell for line in board for cell in line if cell != 0])
    # 全てのマスが埋まった場合
    if currentPiece == boardSize ** 2:
        print(123)
        return True

    # 最終手で最後の人マスを打てる場合
    if currentPiece == (boardSize ** 2) - 1:
        if OthelloLogic.getMoves(board, 1, boardSize) != []:
            print(345)
            return False

    # 双方打つ手なし(互いにパス)
    nextBoard = deepcopy(board)
    if OthelloLogic.getMoves(nextBoard, 1, boardSize) == []:
        if OthelloLogic.getMoves(nextBoard, -1, boardSize) == []:
            print(234)
            return True

    return False


def getBoardHash(board):
    """boardのハッシュ値を計算する

    Args:
       board arg1

    Returns:
        int boardのハッシュ値

    """

    # 自コマ2、他ゴマ1、空き0として3進数として計算する

    counter = 0
    hashSum = 0
    for line in board:
        row = ""
        for cell in line:
            i = 2 if cell == 1 else 1 if cell == -1 else 0
            row += str(i)
            hashSum = hashSum + i * (3 ** counter)
            counter = counter + 1
        print(row)

    return hashSum


def average(arr):
    """平均を返す
    
    Args:
       arr ${1:arg1}

    Returns:
        float 平均

    """

    return sum(arr) / len(arr)
