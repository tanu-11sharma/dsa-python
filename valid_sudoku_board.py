"""
Valid Sudoku Board
------------------
Given a partially filled 9x9 Sudoku board where empty cells are marked ".",
decide whether the filled cells are placed legally. A board is valid when no
row, no column and no 3x3 sub-box contains a repeated digit. The board does
not need to be solvable.

Time:  O(1) -- the board is always 81 cells
Space: O(1)
"""

from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    seen_rows = [set() for _ in range(9)]
    seen_cols = [set() for _ in range(9)]
    seen_boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                continue

            box = (r // 3) * 3 + (c // 3)
            if (
                value in seen_rows[r]
                or value in seen_cols[c]
                or value in seen_boxes[box]
            ):
                return False

            seen_rows[r].add(value)
            seen_cols[c].add(value)
            seen_boxes[box].add(value)

    return True


def _board(rows: List[str]) -> List[List[str]]:
    """Helper to build a board from 9 compact strings."""
    return [list(row) for row in rows]


if __name__ == "__main__":
    good = _board([
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ])
    print(is_valid_sudoku(good))
    # expected output: True

    bad_column = _board([
        "83..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ])
    print(is_valid_sudoku(bad_column))
    # expected output: False

    print(is_valid_sudoku(_board(["." * 9] * 9)))
    # expected output: True
