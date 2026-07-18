"""
Validate Binary Search Tree
-----------------------------
Given the root of a binary tree, determine whether it is a valid binary
search tree. In a valid BST, every node's value must be strictly greater
than all values in its left subtree and strictly less than all values in
its right subtree.

Time:  O(n)
Space: O(h), where h is the height of the tree (recursion stack)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def helper(node: Optional[TreeNode], low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(valid))  # expected output: True

    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(invalid))  # expected output: False

    single_node = TreeNode(1)
    print(is_valid_bst(single_node))  # expected output: True

    print(is_valid_bst(None))  # expected output: True
