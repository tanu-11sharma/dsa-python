"""
Number of Provinces (Union-Find)
-----------------------------------
You are given an n x n adjacency matrix where matrix[i][j] == 1 means
city i and city j are directly connected. A "province" is a maximal
group of cities reachable from one another, directly or indirectly.
Count the number of provinces using a disjoint-set (union-find)
structure with path compression and union by rank.

Time:  O(n^2 * a(n)) -- scanning the matrix dominates; union-find ops are near O(1)
Space: O(n) for the parent and rank arrays
"""


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size

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
        self.count -= 1


def find_number_of_provinces(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.count


if __name__ == "__main__":
    print(find_number_of_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # expected output: 2
    print(find_number_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # expected output: 3
    print(find_number_of_provinces([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # expected output: 1
