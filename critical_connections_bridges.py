"""
Critical Connections In A Network
------------------------------------
A set of n servers is connected by bidirectional cables, forming a
connected undirected graph. A connection is "critical" if removing it
would split the network into two or more disconnected pieces (i.e. it
is a bridge). Find all critical connections using Tarjan's bridge-
finding algorithm: a DFS that tracks each node's discovery time and the
lowest discovery time reachable from it (its "low-link" value); an edge
(u, v) is a bridge exactly when low[v] > discovery[u].

Time:  O(V + E) for the single DFS pass over all vertices and edges.
Space: O(V + E) for the adjacency list, discovery/low-link arrays, and
       recursion stack.
"""

from typing import List, Tuple


def critical_connections(n: int, connections: List[List[int]]) -> List[Tuple[int, int]]:
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * n
    low = [0] * n
    bridges: List[Tuple[int, int]] = []
    timer = [0]

    def dfs(node: int, parent: int) -> None:
        discovery[node] = low[node] = timer[0]
        timer[0] += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.append((node, neighbor))
            else:
                low[node] = min(low[node], discovery[neighbor])

    for start in range(n):
        if discovery[start] == -1:
            dfs(start, -1)

    return bridges


if __name__ == "__main__":
    print(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
    # expected output: [(1, 3)]

    print(critical_connections(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))
    # expected output: [(1, 3)]

    print(critical_connections(2, [[0, 1]]))
    # expected output: [(0, 1)]

    print(critical_connections(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    # expected output: [(3, 4), (2, 3), (1, 2), (0, 1)]
