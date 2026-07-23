"""
Search a 2D Matrix
--------------------
Given an m x n matrix where each row is sorted left to right and the
first integer of each row is greater than the last integer of the
previous row, determine whether a target value exists anywhere in the
matrix.

Time:  O(log(m * n))
Space: O(1)
"""
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


if __name__ == "__main__":
    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(search_matrix(grid, 3))    # expected output: True
    print(search_matrix(grid, 13))   # expected output: False
    print(search_matrix([[1]], 1))   # expected output: True
