import math


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
