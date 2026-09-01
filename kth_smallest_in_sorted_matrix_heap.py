"""
Kth Smallest Element in a Sorted Matrix
------------------------------------------
Given an n x n matrix where every row and every column is sorted in
ascending order, find the k-th smallest element in the matrix using a
min-heap seeded with the first element of each row.

Time:  O(k log n)
Space: O(n)
"""

import heapq
from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[row][0], row, 0) for row in range(min(n, k))]
    heapq.heapify(heap)

    value = matrix[0][0]
    for _ in range(k):
        value, row, col = heapq.heappop(heap)
        if col + 1 < n:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

    return value


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    print(kth_smallest(matrix, 8))  # expected output: 13
    print(kth_smallest(matrix, 1))  # expected output: 1

    matrix2 = [[-5]]
    print(kth_smallest(matrix2, 1))  # expected output: -5
