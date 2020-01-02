import OthelloLogic
import action1
import util
from copy import deepcopy
from pprint import pprint


def action(board, moves):
    """
    
    Args:
       board ${1:arg1}
       moves ${2:arg2}

    Returns:
        move 選択したmove

    """
    pprint(moves)

    # 確定マスではない辺はなるべく取りたい
    sidePos = len(board) - 1
    for move in moves:
        if isCorner(board, move):
            tmpL.append(move)
        elif move[0] == 0 or move[0] == sidePos or move[1] == 0 or move[1] == sidePos:
            if not isStaticPoint(board, move):
                return move

    center = action1.getCenter(board)
    distances = []
    for move in moves:
        distances.append(
            [util.getDistance([move[0], move[1]], [center[0], center[1]]), move]
        )

    sorted(distances, key=lambda x: x[1])

    moves = []
    for distance in distances:
        moves.append(distance[1])

    # 辺の確定マスにはなるべく打たない
    tmpH = []
    tmpL = []
    for move in moves:
        if isStaticPoint(board, move):
            tmpL.append(move)
        else:
            tmpH.append(move)
    tmpH.extend(tmpL)
    moves = tmpH

    # 角はなるべくとらない
    tmpH = []
    tmpL = []
    for move in moves:
        if isCorner(board, move):
            tmpL.append(move)
        else:
            tmpH.append(move)
    tmpH.extend(tmpL)
    moves = tmpH

    return moves[0]


def isCorner(board, move):
    """角かどうかどうか判定する
    
    Args:
       move ${1:arg1}

    Returns:
        bool

    """
    boardSize = len(board) - 1
    l = [
        [0, 0],
        [boardSize, 0],
        [0, boardSize],
        [boardSize, boardSize],
    ]

    for i in l:
        if i == move:
            return True
    return False


def isStaticPoint(board, _move):
    """辺のうち、確定マスになる場合はtrue
    
    Args:
       board 
       moves 

    Returns:
        bool

    """
    move = []
    move.append(_move[1])
    move.append(_move[0])

    # なぜboardはboard[y][x]なのにmovesはmoves[x][y]なのか

    sidePos = len(board) - 1

    # 角
    if isCorner(board, move):
        return True

    # 辺でない場合はfalse
    if not (move[0] == 0 or move[0] == sidePos or move[1] == 0 or move[1] == sidePos):
        return False

    # 横辺
    if move[0] == 0 or move[0] == sidePos:
        # 左に走査して相手駒か空きがあれば左は確定でない
        i = 1
        while True:
            if move[1] - i < 0:
                return True
            if board[move[0]][move[1] - i] != 1:
                break
            i += 1

        # 右に走査して相手駒が空きがあれば右は確定でない
        i = 1
        while True:
            if move[1] + i > sidePos:
                return True
            if board[move[0]][move[1] + i] != 1:
                break
            i += 1

    # 縦辺
    if move[1] == 0 or move[1] == sidePos:
        # 上に走査して相手駒か空きがあれば上は確定でない
        i = 1
        while True:
            if move[0] - i < 0:
                return True
            if board[move[0] - i][move[1]] != 1:
                break
            i += 1

        # 下に走査して相手駒が空きがあれば下は確定でない
        i = 1
        while True:
            if move[0] + i == sidePos:
                return True
            if board[move[0] + i][move[1]] != 1:
                break
            i += 1

    return False


# board = [
#     [1, 1, -1, 1, 1, 1, 1, 0],
#     [1, 1, -1, -1, 1, 1, -1, 0],
#     [1, 1, 1, 1, -1, -1, -1, -1],
#     [1, 1, 1, -1, -1, 1, -1, 0],
#     [1, 1, 1, 1, -1, 1, -1, 0],
#     [-1, -1, -1, -1, 1, -1, 0, 0],
#     [-1, -1, -1, -1, -1, 1, -1, 1],
#     [-1, -1, -1, -1, -1, -1, 1, 1],
# ]

# OthelloLogic.printBoard(board)
# i
# moves = OthelloLogic.getMoves(board, 1, 8)

# print("----")
# util.printMoves(deepcopy(board), moves)


# for move in moves:
#     print("---")
#     util.printMoves(deepcopy(board), moves, move)
#     print(move)
#     print(isStaticPoint(board, move))
