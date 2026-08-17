"""
Check If a Graph Is Bipartite
-----------------------------
Given an undirected graph described as an adjacency list, decide whether its
nodes can be split into two groups so that every edge joins a node of one group
to a node of the other. A breadth-first sweep paints each component with two
alternating labels and fails as soon as an edge links two equally labelled nodes.

Time:  O(V + E)
Space: O(V)
"""

from collections import deque
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """Return True when the undirected graph admits a valid two-colouring."""
    colour = [0] * len(graph)

    for start in range(len(graph)):
        if colour[start] != 0:
            continue

        colour[start] = 1
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if colour[neighbour] == colour[node]:
                    return False
                if colour[neighbour] == 0:
                    colour[neighbour] = -colour[node]
                    queue.append(neighbour)

    return True


if __name__ == "__main__":
    print(is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    # expected output: True

    print(is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    # expected output: False

    print(is_bipartite([[], [2], [1]]))
    # expected output: True
