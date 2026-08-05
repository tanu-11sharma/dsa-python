"""
Height-Balanced Binary Tree Check
---------------------------------
A binary tree is height-balanced when, for every node in the tree, the heights
of its two subtrees differ by at most one. Decide whether a given tree is
balanced. The naive approach recomputes heights repeatedly; instead a single
post-order pass returns each subtree's height and short-circuits as soon as an
imbalance is discovered.

Time:  O(n)
Space: O(h) for the recursion stack, where h is the tree height
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True if every node's subtrees differ in height by at most one."""

    def height(node: Optional[TreeNode]) -> int:
        """Return the node's height, or -1 to signal an imbalance below it."""
        if node is None:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


if __name__ == "__main__":
    balanced = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(is_balanced(balanced))
    # expected output: True

    skewed = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    print(is_balanced(skewed))
    # expected output: False

    print(is_balanced(None))
    # expected output: True

    lopsided = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    print(is_balanced(lopsided))
    # expected output: False
