"""
K Closest Points to Origin
---------------------------
Given a list of 2D points and an integer k, return the k points that are
closest to the origin (0, 0), in any order. Distance is measured using the
standard Euclidean distance formula.

Time:  O(n log k)
Space: O(k)
"""

import heapq
from typing import List, Tuple


def k_closest(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    heap: List[Tuple[int, Tuple[int, int]]] = []

    for x, y in points:
        dist = -(x * x + y * y)  # negate for a max-heap of size k
        if len(heap) < k:
            heapq.heappush(heap, (dist, (x, y)))
        elif dist > heap[0][0]:
            heapq.heapreplace(heap, (dist, (x, y)))

    return [point for _, point in heap]


if __name__ == "__main__":
    print(k_closest([(1, 3), (-2, 2)], 1))  # expected output: [(-2, 2)]
    print(sorted(k_closest([(3, 3), (5, -1), (-2, 4)], 2)))
    # expected output: [(-2, 4), (3, 3)]
    print(k_closest([(0, 0), (1, 1)], 2))  # expected output: [(0, 0), (1, 1)] in any order
