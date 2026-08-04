"""
Rotting Oranges (Multi-Source BFS)
----------------------------------
A grid holds empty cells (0), fresh oranges (1) and rotten oranges (2). Every
minute, each rotten orange spoils every fresh orange directly above, below,
left or right of it. Return the number of minutes until no fresh orange
remains, or -1 if some orange can never rot.

Time:  O(rows * cols)
Space: O(rows * cols)
"""

from collections import deque
from typing import List


def minutes_until_all_rotten(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue: deque = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue and fresh:
        # Process one full "minute" worth of rotten oranges at a time.
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1

    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    print(minutes_until_all_rotten([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    # expected output: 4

    print(minutes_until_all_rotten([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    # expected output: -1

    print(minutes_until_all_rotten([[0, 2]]))
    # expected output: 0
