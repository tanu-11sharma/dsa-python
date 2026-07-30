"""
Copy List With Random Pointer
-------------------------------
Each node of a singly linked list carries a value, a next pointer, and an
extra random pointer that may reference any node in the list or nothing at
all. Build a deep copy: brand new nodes whose next and random pointers mirror
the original structure. Map originals to their clones, then wire the copies.

Time:  O(n)
Space: O(n)
"""

from typing import Dict, List, Optional, Tuple


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional["Node"] = None
        self.random: Optional["Node"] = None


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    clones: Dict[Node, Node] = {}
    node: Optional[Node] = head
    while node is not None:
        clones[node] = Node(node.val)
        node = node.next

    node = head
    while node is not None:
        copy = clones[node]
        copy.next = clones[node.next] if node.next else None
        copy.random = clones[node.random] if node.random else None
        node = node.next

    return clones[head]


def build_list(values: List[int], random_indices: List[Optional[int]]) -> Optional[Node]:
    nodes = [Node(v) for v in values]
    for i, n in enumerate(nodes):
        n.next = nodes[i + 1] if i + 1 < len(nodes) else None
        idx = random_indices[i]
        n.random = nodes[idx] if idx is not None else None
    return nodes[0] if nodes else None


def describe(head: Optional[Node]) -> List[Tuple[int, Optional[int]]]:
    order: Dict[Node, int] = {}
    node = head
    while node is not None:
        order[node] = len(order)
        node = node.next

    out: List[Tuple[int, Optional[int]]] = []
    node = head
    while node is not None:
        out.append((node.val, order[node.random] if node.random else None))
        node = node.next
    return out


if __name__ == "__main__":
    original = build_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copied = copy_random_list(original)
    print(describe(copied))
    # expected output: [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]

    print(copied is original)  # expected output: False
    print(copy_random_list(None))  # expected output: None
    print(describe(copy_random_list(build_list([1, 2], [1, 1]))))
    # expected output: [(1, 1), (2, 1)]
