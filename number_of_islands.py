"""
Number of Islands
------------------
Given a 2D grid of '1's (land) and '0's (water), count how many
islands exist. An island is formed by connecting adjacent lands
horizontally or vertically and is surrounded by water.

Time:  O(rows * cols)
Space: O(rows * cols) (recursion stack / visited set in worst case)
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == "0":
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                islands += 1
                dfs(r, c)

    return islands


if __name__ == "__main__":
    grid1 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    print(num_islands(grid1))
    # expected output: 3

    grid2 = [
        list("111"),
        list("010"),
        list("111"),
    ]
    print(num_islands(grid2))
    # expected output: 1

    grid3 = [list("0000")]
    print(num_islands(grid3))
    # expected output: 0
