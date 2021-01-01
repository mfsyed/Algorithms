"""This is the main file you'll edit.
"""

try:
    from game import board_from_heights
except ModuleNotFoundError:
    pass

# 4 possible rotations for any piece.
ROTATIONS = [0, 1, 2, 3]


def make_move(rows, columns, heights, shape_name, x, rotation):
    """Takes a the tetris board as column heights and applies a particular move.

    Args:
        rows (int): Number of rows in this tetris game.
        columns (int): Number of columns in this tetris game.
        heights (Tuple[int]): List of column heights in the current board.
        shape_name (str): Name of the piece shape (like "L" or "O" etc.)
        x (int): Which column to drop the piece in.
        rotation (int): Rotation of the piece, either 0, 1, 2, or 3.

    Returns:
        Modified heights _after_ the piece at `x` and `rotation` have been dropped.
        `None` if move is invalid.
    """

    board = board_from_heights(heights, rows, columns)

    try:
        board.move(shape_name, x, rotation)
    except ValueError:
        return None

    return tuple(board.skyline())


###
# DO NOT MODIFY ABOVE THIS FILE.
###


def dp(rows, columns, preSuffix, heights, solved = {}):
    if preSuffix == []:
        return []

    if (tuple(preSuffix), heights) in solved:
        return solved[(tuple(preSuffix), heights)]

    new_hs = [(make_move(rows, columns, heights, preSuffix[0], x, rotation), x, rotation) for x in range(columns) for rotation in ROTATIONS]
    legal_hs = [_ for _ in new_hs if _[0] is not None]
    subproblems = [(legalheight[1:], dp(rows, columns, preSuffix[1:], legalheight[0], solved)) for legalheight in legal_hs]
    solvable_sub = [_ for _ in subproblems if _[1] is not None]
    answer = None if len(solvable_sub) == 0 else [solvable_sub[0][0]] + solvable_sub[0][1]
    solved[(tuple(preSuffix), heights)] = answer
    return answer

def solver(rows, columns, shape_sequence):
    """Solve a given tetris game.

    Args:
        rows (int): Number of rows in this game.
        columns (int): Number of columns in this game.
        shape_sequence (List[str]): List of shape names to come (This list is of size n).
                                    e.g. `shape_sequence = ["L", "O", "I", "L"]`

    Returns:
        A list of `(x, rotation)` pairs corresponding to the ideal moves to be made to survive.
        `None` if there is no possible way to survive.
    """
    hs = tuple(0 for _ in range(columns))
    return dp(rows, columns, shape_sequence, hs)
