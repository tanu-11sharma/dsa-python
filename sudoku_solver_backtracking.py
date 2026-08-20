"""
Sudoku Solver
-------------
Complete a partially filled 9x9 Sudoku grid so that every row, every column and
each of the nine 3x3 boxes contains the digits 1 through 9 exactly once. Blank
cells are marked with '.'. The grid is solved in place; the function reports
whether a valid completion exists.

Time:  O(9^m) worst case, where m is the number of blank cells
Space: O(m) for the recursion stack
"""

from __future__ import annotations

from typing import List, Set, Tuple

EMPTY = "."
DIGITS = "123456789"


def solve_sudoku(board: List[List[str]]) -> bool:
    """Fill the board in place. Return True if the puzzle could be solved."""
    rows: List[Set[str]] = [set() for _ in range(9)]
    cols: List[Set[str]] = [set() for _ in range(9)]
    boxes: List[Set[str]] = [set() for _ in range(9)]
    blanks: List[Tuple[int, int]] = []

    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == EMPTY:
                blanks.append((r, c))
            else:
                rows[r].add(value)
                cols[c].add(value)
                boxes[(r // 3) * 3 + c // 3].add(value)

    def backtrack(index: int) -> bool:
        if index == len(blanks):
            return True

        r, c = blanks[index]
        box = (r // 3) * 3 + c // 3

        for digit in DIGITS:
            if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                continue

            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)

            if backtrack(index + 1):
                return True

            board[r][c] = EMPTY
            rows[r].discard(digit)
            cols[c].discard(digit)
            boxes[box].discard(digit)

        return False

    return backtrack(0)


if __name__ == "__main__":
    puzzle = [list(row) for row in [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ]]
    print(solve_sudoku(puzzle))  # expected output: True
    print("".join(puzzle[0]))  # expected output: 534678912
    print("".join(puzzle[8]))  # expected output: 345286179
