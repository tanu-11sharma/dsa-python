"""
Maximum Width of Binary Tree
-----------------------------------
Given the root of a binary tree, find the maximum width among all levels.
The width of a level is the distance between the leftmost and rightmost
non-null nodes, counting the null nodes that would sit between them as
if the tree were a complete binary tree (i.e. positions are indexed the
way a heap array would index them).

Time:  O(n), one pass over every node via BFS
Space: O(w), where w is the maximum number of nodes at any level
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_width(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    widest = 0
    queue = deque([(root, 0)])
    while queue:
        level_size = len(queue)
        _, first_index = queue[0]
        last_index = first_index
        for _ in range(level_size):
            node, index = queue.popleft()
            last_index = index
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
        widest = max(widest, last_index - first_index + 1)
    return widest


if __name__ == "__main__":
    #        1
    #       / \
    #      3   2
    #       \     \
    #        5     9
    root = TreeNode(1, TreeNode(3, None, TreeNode(5)), TreeNode(2, None, TreeNode(9)))
    print(max_width(root))  # expected output: 3

    single = TreeNode(1)
    print(max_width(single))  # expected output: 1

    left_leaning = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(max_width(left_leaning))  # expected output: 1

    print(max_width(None))  # expected output: 0
