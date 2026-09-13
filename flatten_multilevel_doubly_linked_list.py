"""
Flatten a Multilevel Doubly Linked List
--------------------------------------------
Given a doubly linked list where, besides the next and previous
pointers, a node may point to a separate doubly linked list via a
child pointer, flatten the whole structure into a single-level list
using next and previous pointers, in depth-first order.

Time:  O(n)
Space: O(d), d = maximum nesting depth
"""

from typing import Optional


class Node:
    def __init__(self, val: int, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    stack = [head]
    prev: Optional[Node] = None

    while stack:
        node = stack.pop()

        if prev:
            prev.next = node
            node.prev = prev

        if node.next:
            stack.append(node.next)

        if node.child:
            stack.append(node.child)
            node.child = None

        prev = node

    return head


def to_list(head: Optional[Node]) -> list:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    child = Node(7, next=Node(8, next=Node(9)))
    main_list = Node(1, next=Node(2, child=child))
    print(to_list(flatten(main_list)))  # expected output: [1, 2, 7, 8, 9]

    single = Node(5)
    print(to_list(flatten(single)))  # expected output: [5]

    print(to_list(flatten(None)))  # expected output: []
