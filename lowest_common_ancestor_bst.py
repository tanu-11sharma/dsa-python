"""
Lowest Common Ancestor of a Binary Search Tree
------------------------------------------------
Given the root of a binary search tree and two nodes p and q that are
guaranteed to exist in the tree, find their lowest common ancestor:
the deepest node that has both p and q as descendants (a node is
allowed to be a descendant of itself).

Time:  O(h), where h is the height of the tree
Space: O(1)
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return None


def _insert(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = _insert(root.left, val)
    else:
        root.right = _insert(root.right, val)
    return root


def _build_bst(values: list) -> Optional[TreeNode]:
    root = None
    for v in values:
        root = _insert(root, v)
    return root


if __name__ == "__main__":
    tree = _build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5])
    p, q = tree.left, tree.right  # nodes with values 2 and 8
    print(lowest_common_ancestor(tree, p, q).val)
    # expected output: 6

    p, q = tree.left, tree.left.right  # nodes with values 2 and 4
    print(lowest_common_ancestor(tree, p, q).val)
    # expected output: 2

    p, q = tree.left.right.left, tree.left.right.right  # values 3 and 5
    print(lowest_common_ancestor(tree, p, q).val)
    # expected output: 4
