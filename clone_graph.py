"""
Clone Graph
------------
Given a reference to a node in a connected, undirected graph (where each
node stores a value and a list of neighbors), return a deep copy of the
entire graph. The cloned graph must not share any node objects with the
original.

Time:  O(n + e), n nodes and e edges
Space: O(n)
"""

from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    clones: Dict[Node, Node] = {}

    def dfs(original: Node) -> Node:
        if original in clones:
            return clones[original]

        copy = Node(original.val)
        clones[original] = copy
        for neighbor in original.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)


def build_graph(adjacency: List[List[int]]) -> Optional[Node]:
    """Helper: builds a graph from a 1-indexed adjacency list, for testing."""
    if not adjacency:
        return None
    nodes = {i: Node(i) for i in range(1, len(adjacency) + 1)}
    for i, neighbors in enumerate(adjacency, start=1):
        nodes[i].neighbors = [nodes[j] for j in neighbors]
    return nodes[1]


def to_adjacency(node: Optional[Node]) -> List[List[int]]:
    """Helper: flattens a graph back into a 1-indexed adjacency list."""
    if node is None:
        return []
    seen: Dict[int, List[int]] = {}
    stack = [node]
    visited_nodes = {node.val: node}
    while stack:
        current = stack.pop()
        seen[current.val] = sorted(n.val for n in current.neighbors)
        for neighbor in current.neighbors:
            if neighbor.val not in visited_nodes:
                visited_nodes[neighbor.val] = neighbor
                stack.append(neighbor)
    return [seen[i] for i in sorted(seen)]


if __name__ == "__main__":
    g1 = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    print(to_adjacency(clone_graph(g1)))  # expected output: [[2, 4], [1, 3], [2, 4], [1, 3]]

    g2 = build_graph([[]])
    print(to_adjacency(clone_graph(g2)))  # expected output: [[]]

    print(clone_graph(None))  # expected output: None
