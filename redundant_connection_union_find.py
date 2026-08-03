"""
Redundant Connection In An Undirected Graph
-------------------------------------------
You are given a connected undirected graph built by adding edges one at a
time to a set of n labelled nodes. Exactly one edge is extra, meaning the
graph contains a single cycle. Return the extra edge that, when removed,
turns the graph back into a tree. If several edges qualify, return the one
that appeared last in the input.

Time:  O(n * alpha(n)) which is effectively linear
Space: O(n)
"""

from typing import List, Tuple


class DisjointSet:
    """Union-Find with path compression and union by size."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, a: int, b: int) -> bool:
        """Merge the two sets; return False if they were already joined."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


def find_redundant_connection(edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    if not edges:
        raise ValueError("edges must be non-empty")

    dsu = DisjointSet(len(edges) + 1)
    for u, v in edges:
        if not dsu.union(u, v):
            return (u, v)
    raise ValueError("no redundant edge found; graph is already a tree")


if __name__ == "__main__":
    print(find_redundant_connection([(1, 2), (1, 3), (2, 3)]))  # expected output: (2, 3)
    print(find_redundant_connection([(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)]))  # expected output: (1, 4)
    print(find_redundant_connection([(1, 3), (3, 4), (1, 4), (1, 2)]))  # expected output: (1, 4)
