"""
Binary Tree Level Order Traversal
-----------------------------------
Given the root of a binary tree, return the values of its nodes grouped
level by level, from top to bottom, left to right within each level.
Implemented with an iterative breadth-first traversal using a queue.

Time:  O(n)
Space: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result: List[List[int]] = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))  # expected output: [[3], [9, 20], [15, 7]]
    print(level_order(None))  # expected output: []
    single = TreeNode(1)
    print(level_order(single))  # expected output: [[1]]
    left_only = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(level_order(left_only))  # expected output: [[1], [2], [3]]
