"""
Graph BFS & DFS
----------------
Breadth-first and depth-first traversal of a graph represented as an
adjacency list (dict of node -> list of neighbors).

Time:  O(V + E)
Space: O(V)
"""
from collections import deque
from typing import Dict, List


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = set()
    order = []

    def visit(node: str) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }
    print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D', 'E']
    print(dfs(graph, "A"))  # ['A', 'B', 'D', 'C', 'E']
