"""
Serialize and Deserialize a Binary Tree
---------------------------------------
Design a pair of routines that turn a binary tree into one flat string and
rebuild the identical tree from that string. The encoding must round-trip
exactly, preserving both the values and the shape of the tree.
A preorder walk that writes an explicit marker for every empty subtree works.

Time:  O(n) for serialize and for deserialize
Space: O(n) for the encoded string plus the recursion stack
"""

from typing import Iterator, List, Optional

NULL_MARKER = "#"


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


def serialize(root: Optional[TreeNode]) -> str:
    """Encode a binary tree as a comma separated preorder walk."""
    parts: List[str] = []

    def walk(node: Optional[TreeNode]) -> None:
        if node is None:
            parts.append(NULL_MARKER)
            return
        parts.append(str(node.val))
        walk(node.left)
        walk(node.right)

    walk(root)
    return ",".join(parts)


def deserialize(data: str) -> Optional[TreeNode]:
    """Rebuild the tree produced by serialize."""
    tokens: Iterator[str] = iter(data.split(","))

    def build() -> Optional[TreeNode]:
        token = next(tokens)
        if token == NULL_MARKER:
            return None
        node = TreeNode(int(token))
        node.left = build()
        node.right = build()
        return node

    return build()


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

    encoded = serialize(tree)
    print(encoded)
    # expected output: 1,2,#,#,3,4,#,#,5,#,#

    print(serialize(deserialize(encoded)) == encoded)
    # expected output: True

    print(serialize(None))
    # expected output: #

    print(deserialize(NULL_MARKER) is None)
    # expected output: True
