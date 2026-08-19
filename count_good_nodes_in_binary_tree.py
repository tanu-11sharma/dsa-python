"""
Count Good Nodes in a Binary Tree
---------------------------------
Call a node "good" when no node on the path from the root down to it
holds a strictly larger value. Given the root of a binary tree, count how
many good nodes it contains. A single depth-first walk that carries the
largest value seen so far along each path answers this in one pass.

Time:  O(n)
Space: O(h), where h is the height of the tree
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


def count_good_nodes(root: Optional[TreeNode]) -> int:
    def walk(node: Optional[TreeNode], best: int) -> int:
        if node is None:
            return 0
        found = 1 if node.val >= best else 0
        best = max(best, node.val)
        return found + walk(node.left, best) + walk(node.right, best)

    if root is None:
        return 0
    return walk(root, root.val)


if __name__ == "__main__":
    #       3
    #      / \
    #     1   4
    #    /   / \
    #   3   1   5
    tree = TreeNode(
        3,
        TreeNode(1, TreeNode(3)),
        TreeNode(4, TreeNode(1), TreeNode(5)),
    )
    print(count_good_nodes(tree))  # expected output: 4

    #     3
    #    /
    #   3
    #  / \
    # 4   2
    print(count_good_nodes(TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))))
    # expected output: 3

    print(count_good_nodes(TreeNode(9)))  # expected output: 1
    print(count_good_nodes(None))         # expected output: 0
