"""
Shortest Bridge Between Islands
--------------------------------
Given a binary grid containing exactly two islands (groups of orthogonally
connected 1s), find the minimum number of 0-cells that must be flipped to
connect the two islands into a single island.

Time:  O(rows * cols)
Space: O(rows * cols)
"""

from collections import deque
from typing import List


def shortest_bridge(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def neighbors(r, c):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def find_first_land():
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return r, c
        return None

    def mark_island(sr, sc):
        frontier = deque()
        stack = [(sr, sc)]
        visited[sr][sc] = True
        while stack:
            cr, cc = stack.pop()
            frontier.append((cr, cc))
            for nr, nc in neighbors(cr, cc):
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        return frontier

    sr, sc = find_first_land()
    frontier = mark_island(sr, sc)

    steps = 0
    while frontier:
        for _ in range(len(frontier)):
            r, c = frontier.popleft()
            for nr, nc in neighbors(r, c):
                if visited[nr][nc]:
                    continue
                if grid[nr][nc] == 1:
                    return steps
                visited[nr][nc] = True
                frontier.append((nr, nc))
        steps += 1

    return -1


if __name__ == "__main__":
    print(shortest_bridge([
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0],
    ]))  # expected output: 1

    print(shortest_bridge([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]))  # expected output: 3

    print(shortest_bridge([
        [1, 0],
        [0, 1],
    ]))  # expected output: 1
