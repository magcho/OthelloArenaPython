def initStack():
    """stackをグローバル空間に定義する


    """
    global MOVE_STACK
    global BOARD_STACK
    MOVE_STACK = []
    BOARD_STACK = []


def moveStack(moves):
    """stackにobj(Array)を積む
    
    Args:
       stack 積む対象のスタック
       obj 積み荷

    """
    global MOVE_STACK
    MOVE_STACK.append(moves)


def movepPop():
    """stackからarrを一つpop

    Returns:
        arr

    """

    return MOVE_STACK.pop(len(MOVE_STACK))


def boardStack(board):
    """boardをスタックに積む

    Args:
       board arg1


    """
    BOARD_STACK.append(board)


def boardPop():
    """boardをスタックから持ってくる

    Returns:
        board

    """

    return BOARD_STACK.pop(len(BOARD_STACK))
