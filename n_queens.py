"""
N-Queens
-----------------------------------
Place N chess queens on an N x N board so that no two queens share a row,
column, or diagonal. Return every distinct board arrangement, each
rendered as a list of strings where 'Q' marks a queen and '.' an empty
square. Backtrack column by column, tracking which rows and diagonals
are already under attack.

Time:  O(N!) in the worst case
Space: O(N) for the recursion stack and attack-tracking sets
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    solutions: List[List[str]] = []
    cols = set()
    diagonals = set()      # row - col is constant along a "\\" diagonal
    anti_diagonals = set()  # row + col is constant along a "/" diagonal
    placement = [-1] * n

    def backtrack(row: int) -> None:
        if row == n:
            board = []
            for r in range(n):
                line = ["."] * n
                line[placement[r]] = "Q"
                board.append("".join(line))
            solutions.append(board)
            return

        for col in range(n):
            if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                continue

            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            placement[row] = col

            backtrack(row + 1)

            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)

    backtrack(0)
    return solutions


if __name__ == "__main__":
    print(len(solve_n_queens(4)))  # expected output: 2
    print(len(solve_n_queens(1)))  # expected output: 1
    print(len(solve_n_queens(8)))  # expected output: 92
    print(solve_n_queens(4)[0])  # expected output: ['.Q..', '...Q', 'Q...', '..Q.']
