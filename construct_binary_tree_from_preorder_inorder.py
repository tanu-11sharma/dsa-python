"""
Construct Binary Tree from Preorder and Inorder Traversal
------------------------------------------------------------
Given two integer arrays holding the preorder and inorder traversal of a
binary tree with unique values, rebuild and return the original tree. The
inorder sequence tells us how to split each subtree; the preorder sequence
tells us the root order in which to consume values.

Time:  O(n)
Space: O(n)
"""
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    index_of: Dict[int, int] = {val: i for i, val in enumerate(inorder)}
    pre_pos = [0]

    def helper(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        root_val = preorder[pre_pos[0]]
        pre_pos[0] += 1
        root = TreeNode(root_val)
        mid = index_of[root_val]
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(inorder) - 1)


def level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    out: List[Optional[int]] = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(level_order(tree))  # expected output: [3, 9, 20, None, None, 15, 7]
    tree2 = build_tree([-1], [-1])
    print(level_order(tree2))  # expected output: [-1]
    tree3 = build_tree([1, 2, 3], [2, 1, 3])
    print(level_order(tree3))  # expected output: [1, 2, 3]
