"""
Number of Connected Components in an Undirected Graph
----------------------------------------------------------
Given n nodes labeled 0 to n-1 and a list of undirected edges, count
how many connected components the graph has using union-find
(disjoint set union) with path compression and union by rank.

Time:  O(n + e * a(n))
Space: O(n)
"""

from typing import List, Tuple


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return

        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

        self.components -= 1


def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a, b)
    return uf.components


if __name__ == "__main__":
    print(count_components(5, [(0, 1), (1, 2), (3, 4)]))  # expected output: 2
    print(count_components(5, [(0, 1), (1, 2), (2, 3), (3, 4)]))  # expected output: 1
    print(count_components(4, []))  # expected output: 4
