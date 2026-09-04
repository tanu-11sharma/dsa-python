"""
Binary Tree Maximum Path Sum
------------------------------
A "path" in a binary tree is any sequence of nodes connected by parent-child
edges where no node repeats; it does not need to pass through the root and
does not need to end at a leaf. Given the root of a binary tree, return the
largest possible sum of node values along any path.

Time:  O(n)
Space: O(h), where h is the height of the tree (recursion stack)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0

        # Only extend into a child subtree if it contributes positively.
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Best path that "bends" through this node (candidate for the answer).
        best = max(best, node.val + left_gain + right_gain)

        # Best path a parent could extend through this node (straight line only).
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(best)


if __name__ == "__main__":
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(max_path_sum(tree1))  # expected output: 6

    tree2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_path_sum(tree2))  # expected output: 42

    tree3 = TreeNode(-3)
    print(max_path_sum(tree3))  # expected output: -3

    tree4 = TreeNode(2, TreeNode(-1))
    print(max_path_sum(tree4))  # expected output: 2
