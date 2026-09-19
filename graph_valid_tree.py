"""
Graph Valid Tree
------------------
Given `n` nodes labeled 0 to n-1 and a list of undirected edges, decide
whether the resulting graph forms a valid tree. A valid tree is
connected and has no cycles, which for n nodes means it must have
exactly n - 1 edges and every node must be reachable from any other.

Time:  O(n + e) with union-find using path compression and union by
       rank (e = number of edges)
Space: O(n) for the union-find parent/rank arrays
"""

from __future__ import annotations


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False  # already connected -> adding this edge makes a cycle

        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True


def valid_tree(n: int, edges: list[tuple[int, int]]) -> bool:
    if len(edges) != n - 1:
        return False

    uf = UnionFind(n)
    for a, b in edges:
        if not uf.union(a, b):
            return False

    return True


if __name__ == "__main__":
    print(valid_tree(5, [(0, 1), (0, 2), (0, 3), (1, 4)]))  # expected output: True
    print(valid_tree(5, [(0, 1), (1, 2), (2, 3), (1, 3), (1, 4)]))  # expected output: False
    print(valid_tree(4, [(0, 1), (2, 3)]))  # expected output: False
    print(valid_tree(1, []))  # expected output: True
