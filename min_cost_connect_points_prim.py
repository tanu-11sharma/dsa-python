"""
Minimum Cost to Connect All Points
----------------------------------
Given a set of points on a 2D plane, join them into a single connected network
for the lowest possible total cost, where laying a wire between two points
costs their Manhattan distance. The answer is the weight of a minimum spanning
tree, grown here one point at a time with Prim's algorithm and a min-heap.

Time:  O(n^2 log n)
Space: O(n^2)
"""

from __future__ import annotations

import heapq
from typing import List, Tuple


def min_cost_connect_points(points: List[Tuple[int, int]]) -> int:
    """Return the cheapest total Manhattan wiring that connects every point."""
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    total = 0
    connected = 0

    # Heap entries are (cost to reach a point, index of that point).
    frontier: List[Tuple[int, int]] = [(0, 0)]

    while frontier and connected < n:
        cost, index = heapq.heappop(frontier)
        if visited[index]:
            continue

        visited[index] = True
        total += cost
        connected += 1

        x1, y1 = points[index]
        for neighbour in range(n):
            if visited[neighbour]:
                continue
            x2, y2 = points[neighbour]
            heapq.heappush(frontier, (abs(x1 - x2) + abs(y1 - y2), neighbour))

    return total


if __name__ == "__main__":
    print(min_cost_connect_points([(0, 0), (2, 2), (3, 10), (5, 2), (7, 0)]))  # expected output: 20
    print(min_cost_connect_points([(3, 12), (-2, 5), (-4, 1)]))  # expected output: 18
    print(min_cost_connect_points([(0, 0)]))  # expected output: 0
