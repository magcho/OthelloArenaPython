import action4

"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""


def getAction(board, moves):
    return action4.action(board, moves)
    # return action3.action(board, moves)
    # 渡されたMovesの中からランダムで返り値として返却する。
    # index = random.randrange(len(moves))
    # return moves[index]
