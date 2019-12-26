import random
import OthelloLogic  # コマをひっくり返したり、合法手を取得する関数が入ってます
import copy  # コードがうまく動くようになるおまじない

"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""


def getAction(board, moves):
    # オセロ番のサイズを変数に格納
    board_size = len(board[0])
    # オセロ盤の角の座標を配列に格納
    squares = [
        [0, board_size - 1],
        [board_size - 1, 0],
        [0, board_size - 1],
        [board_size - 1, board_size - 1],
    ]

    # もしも角がとれるなら角に手を打つ
    # for文で角の座標が引数moves内に存在するかどうかを調べる
    for s in squares:
        if s in moves:
            index = moves.index(s)
            return moves[index]

    # 相手の合法手の最小数を格納する変数（最小値なので初期値は適当に大きく）
    min_enemy_moves_length = 100
    # 返す手のindex(配列の添字)
    index = 0

    # for文で全ての手を打ってみる
    for m in moves:

        # 選択した手を打つ関数
        # 関数:execute
        # 返り値:盤面の状況（ちょうどこのOthelloActionの引数であるboardと同じ感じ）
        # 引数:board:（盤面の状態),move:打つ手(moves配列の中身),player:打つプレイヤー(1だと自分,-1だと相手),size:オセロ盤のサイズ

        # 引数として渡すboardにはdeepcopy関数を使用してください！！
        # deepcopyをしないでboardを渡すとpythonの仕様でおかしなことになります（設計が悪かったですごめんなさい）
        # 詳しくはオブジェクトIDで調べてもらえば...!
        board_next = OthelloLogic.execute(copy.deepcopy(board), m, 1, board_size)

        # 自分の手を打った後の相手の合法手を取得する関数
        # 関数:getMoves
        # 返り値:moves(選択したプレイヤーの合法手配列)
        # 引数:board(盤面の状態),player(どちらのプレイヤーの合法手を取得するか、1だと自分,-1だと相手,size:オセロ盤の大きさ)
        moves_next = OthelloLogic.getMoves(copy.deepcopy(board_next), -1, board_size)

        # 取得した相手の合法手の数が現在の最小値よりも低ければ最小値を更新
        if min_enemy_moves_length > len(moves_next):
            min_enemy_moves_length = len(moves_next)
            # 返す手のindexを更新
            index = moves.index(m)

    # 最小値の配列indexを返却して手を実行
    return moves[index]
