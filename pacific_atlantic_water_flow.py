"""
Pacific Atlantic Water Flow
---------------------------
A rectangular island is described by a grid of cell heights. Water on a cell can
flow to any of the four orthogonally adjacent cells whose height is less than or
equal to the current cell's height. The Pacific ocean touches the island's top
and left edges; the Atlantic ocean touches the bottom and right edges.
Return the coordinates of every cell from which water can reach BOTH oceans.

Time:  O(m * n)
Space: O(m * n)
"""

from typing import List, Set, Tuple


def pacific_atlantic(heights: List[List[int]]) -> List[Tuple[int, int]]:
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])

    def flood(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        """Walk uphill from every ocean-touching cell to find its drainage basin."""
        seen: Set[Tuple[int, int]] = set(starts)
        stack = list(starts)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]
                ):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + [
        (r, cols - 1) for r in range(rows)
    ]

    both = flood(pacific_starts) & flood(atlantic_starts)
    return sorted(both)


if __name__ == "__main__":
    grid = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(pacific_atlantic(grid))
    # expected output: [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]

    print(pacific_atlantic([[1]]))
    # expected output: [(0, 0)]

    print(pacific_atlantic([]))
    # expected output: []
