"""
Right Side View Of A Binary Tree
--------------------------------
Imagine standing to the right of a binary tree and looking at it. Return the
values of the nodes you can see, ordered from the top of the tree down.
Exactly one node is visible per level: the rightmost node on that level.
A breadth-first sweep records the last node dequeued on each level.

Time:  O(n)
Space: O(w) where w is the maximum width of the tree
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    visible: List[int] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for index in range(level_size):
            node = queue.popleft()
            if index == level_size - 1:
                visible.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return visible


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a level-order list where None marks a missing child."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == "__main__":
    print(right_side_view(build_tree([1, 2, 3, None, 5, None, 4])))  # expected output: [1, 3, 4]
    print(right_side_view(build_tree([1, None, 3])))                 # expected output: [1, 3]
    print(right_side_view(build_tree([1, 2, None, 4])))              # expected output: [1, 2, 4]
    print(right_side_view(None))                                     # expected output: []
