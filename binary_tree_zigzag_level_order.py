"""
Binary Tree Zigzag Level Order Traversal
-----------------------------------------
Given the root of a binary tree, return its node values grouped by
level, alternating the reading direction each level: the first level
left-to-right, the next right-to-left, and so on.

Time:  O(n)
Space: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    result: List[List[int]] = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_values = deque()

        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level_values.append(node.val)
            else:
                level_values.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_values))
        left_to_right = not left_to_right

    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(zigzag_level_order(root))  # expected output: [[3], [20, 9], [15, 7]]

    single = TreeNode(1)
    print(zigzag_level_order(single))  # expected output: [[1]]

    print(zigzag_level_order(None))  # expected output: []
