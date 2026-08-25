"""
Kth Smallest Element in a BST
-------------------------------
Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) stored among all the tree's nodes. An in-order
traversal of a BST visits values in ascending order, so an iterative
in-order walk that stops after the kth visit solves this without sorting
or allocating the full list of values.

Time:  O(h + k), where h is the tree height
Space: O(h) for the explicit stack
"""

from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack: list[TreeNode] = []
    node = root
    count = 0

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right

    raise ValueError("k is larger than the number of nodes in the tree")


if __name__ == "__main__":
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(kth_smallest(root, 3))  # expected output: 3
    print(kth_smallest(root, 1))  # expected output: 1
    print(kth_smallest(root, 6))  # expected output: 6
