"""
Connect Ropes for Minimum Cost
---------------------------------
You are given the lengths of several ropes. Connecting two ropes costs an
amount equal to the sum of their lengths, and the resulting rope can be
connected again with others. Determine the minimum total cost to connect
all ropes into a single rope. Always combining the two currently-shortest
ropes (via a min-heap) yields the optimal total cost.

Time:  O(n log n)
Space: O(n)
"""

import heapq
from typing import List


def min_cost_to_connect_ropes(lengths: List[int]) -> int:
    if len(lengths) <= 1:
        return 0

    heap = list(lengths)
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = first + second
        total_cost += combined
        heapq.heappush(heap, combined)

    return total_cost


if __name__ == "__main__":
    print(min_cost_to_connect_ropes([4, 3, 2, 6]))  # expected output: 29
    print(min_cost_to_connect_ropes([1, 8, 3, 5]))  # expected output: 30
    print(min_cost_to_connect_ropes([1, 2, 5, 10, 35, 89]))  # expected output: 224
    print(min_cost_to_connect_ropes([7]))  # expected output: 0
