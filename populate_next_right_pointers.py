"""
Populate Next Right Pointers
-----------------------------
Given a perfect binary tree where every node also has a `next` pointer,
connect each node to its immediate right neighbor on the same level.
The last node in each level should point to None.

Time:  O(n)
Space: O(1) (excluding the O(n) recursion/output structures used for demo)
"""

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: "Optional[Node]" = None,
                 right: "Optional[Node]" = None, next: "Optional[Node]" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Optional[Node]) -> Optional[Node]:
    leftmost = root
    while leftmost and leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root


def level_order_with_next(root: Optional[Node]) -> list[list[int]]:
    """Helper to visualize the next pointers level by level."""
    levels = []
    node = root
    while node:
        level = []
        current = node
        next_level_start = None
        while current:
            level.append(current.val)
            if next_level_start is None:
                next_level_start = current.left
            current = current.next
        levels.append(level)
        node = next_level_start
    return levels


def build_perfect_tree(values: list[int]) -> Optional[Node]:
    if not values:
        return None
    nodes = [Node(v) for v in values]
    n = len(nodes)
    for i in range(n):
        left_idx, right_idx = 2 * i + 1, 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        if right_idx < n:
            nodes[i].right = nodes[right_idx]
    return nodes[0]


if __name__ == "__main__":
    tree1 = build_perfect_tree([1, 2, 3, 4, 5, 6, 7])
    connect(tree1)
    print(level_order_with_next(tree1))  # expected output: [[1], [2, 3], [4, 5, 6, 7]]

    tree2 = build_perfect_tree([1, 2, 3])
    connect(tree2)
    print(level_order_with_next(tree2))  # expected output: [[1], [2, 3]]

    tree3 = build_perfect_tree([1])
    connect(tree3)
    print(level_order_with_next(tree3))  # expected output: [[1]]

    tree4 = build_perfect_tree([])
    connect(tree4)
    print(level_order_with_next(tree4))  # expected output: []
