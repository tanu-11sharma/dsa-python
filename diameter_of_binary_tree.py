"""
Diameter of Binary Tree
--------------------------
Given the root of a binary tree, return the length (measured in edges) of
the longest path between any two nodes in the tree. This path may or may
not pass through the root.

Time:  O(n)
Space: O(h) recursion stack, where h is the tree height
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def depth(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter


if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(diameter_of_binary_tree(root))          # expected output: 3
    print(diameter_of_binary_tree(TreeNode(1)))   # expected output: 0
    print(diameter_of_binary_tree(None))          # expected output: 0
