"""
Last Stone Weight (Max-Heap Simulation)
---------------------------------------
A pile of stones is repeatedly smashed: the two heaviest stones are taken out,
and if their weights differ, a stone weighing the difference is dropped back
into the pile. Return the weight of the single stone left at the end, or 0 if
the pile empties. Repeatedly finding the two largest stones is exactly what a
max-heap is for; Python's heapq is a min-heap, so weights are negated.

Time:  O(n log n)
Space: O(n)
"""

import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    """Return the weight of the remaining stone, or 0 if none remains."""
    if not stones:
        return 0

    # Negate so the smallest value in the min-heap is the heaviest stone.
    heap = [-weight for weight in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        heaviest = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if heaviest != second:
            heapq.heappush(heap, -(heaviest - second))

    return -heap[0] if heap else 0


if __name__ == "__main__":
    print(last_stone_weight([2, 7, 4, 1, 8, 1]))
    # expected output: 1

    print(last_stone_weight([3, 3]))
    # expected output: 0

    print(last_stone_weight([10]))
    # expected output: 10

    print(last_stone_weight([]))
    # expected output: 0
