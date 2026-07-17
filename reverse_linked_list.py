"""
Reverse a Singly Linked List
-----------------------------
Reverse a singly linked list iteratively.

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def build_list(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    print(to_list(reversed_head))  # [5, 4, 3, 2, 1]
