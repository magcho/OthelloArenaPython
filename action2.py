import random
import OthelloLogic
import copy

# user lib
import util

"""
引数について
board:現在の盤面の状態
moves:現在の合法手の一覧
詳しい説明はサイトのHomeページをご覧ください。
"""


def action(board, moves):
    getAction(board, moves)


def getAction(board, moves):
    return MyGetAction(board, 0, evaluationFunc, 2, 5, 8)


def MyGetAction(board, count, func, maxDepth, maxChoice, size):
    getMoves = OthelloLogic.getMoves
    execute = OthelloLogic.execute
    moves = getMoves(board, 1, size)
    evaluation = []
    result = []
    # もしパスの場合は[-1,-1]とする
    if len(moves) == 0:
        moves = [[-1, -1]]
    # 評価関数で枝切りの候補を探す
    for amove in moves:
        temp = [amove, func(board, amove, size)]
        evaluation.append(temp)

        # 評価の高い順にソート
    evaluation.sort(key=lambda x: x[1] * -1)
    # 石を置く場所の候補がmaxChoiceより多い場合は枝切り
    if len(evaluation) > maxChoice:
        temp = evaluation[:maxChoice]
        evaluation = temp
    # count == maxDepthなら、つまり探索を終了する深さまで達したら探索を打ち切る
    if count == maxDepth:
        # count == 0なら評価の高さではなく石を置く座標を返す
        if count == 0:
            return evaluation[0][0]
        return evaluation[0][1] * -1
    # 再帰的に探索を続ける
    for amove in evaluation:
        nextBoard = copy.deepcopy(board)
        # パスで場合は石を置いて盤面を更新する
        if amove[0][0] != -1:
            execute(nextBoard, amove[0], 1, size)
        reverse(nextBoard, size)
        point = MyGetAction(nextBoard, count + 1, func, maxDepth, maxChoice, size)
        result.append([amove[0], point])
    result.sort(key=lambda x: x[1] * -1)
    if count == 0:
        return result[0][0]
    return result[0][1] * -1


def reverse(board, size):
    for i in range(size):
        for j in range(size):
            board[i][j] *= -1


def evaluationFunc(board, target, size):
    nextBoard = OthelloLogic.execute(copy.deepcopy(board), target, 1, size)

    boardScore = 0
    for i in range(8):
        for j in range(8):
            boardScore = boardScore + util.getDistance([4, 4], [i, j]) * board[i][j]
    return boardScore
