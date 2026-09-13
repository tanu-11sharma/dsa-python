"""
Binary Tree Vertical Order Traversal
-----------------------------------------
Given the root of a binary tree, group its node values into vertical
columns based on horizontal distance from the root, and return the
columns ordered from leftmost to rightmost. Within a column, values
appear in top-to-bottom, left-to-right order.

Time:  O(n log n)
Space: O(n)
"""

from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    columns = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        columns[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [columns[col] for col in sorted(columns)]


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(vertical_order(root))  # expected output: [[9], [3, 15], [20], [7]]

    single = TreeNode(1)
    print(vertical_order(single))  # expected output: [[1]]

    print(vertical_order(None))  # expected output: []
