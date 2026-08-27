"""
Swap Nodes in Pairs
---------------------
Given a singly linked list, swap every two adjacent nodes and return
the head of the modified list. Nodes themselves must be exchanged
(not just their values), and a list with an odd number of nodes
leaves the final node untouched.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def from_list(values: list) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(swap_pairs(from_list([1, 2, 3, 4]))))  # expected output: [2, 1, 4, 3]
    print(to_list(swap_pairs(from_list([1, 2, 3]))))  # expected output: [2, 1, 3]
    print(to_list(swap_pairs(from_list([]))))  # expected output: []
