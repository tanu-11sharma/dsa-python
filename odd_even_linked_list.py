"""
Group Linked List Nodes by Odd and Even Position
---------------------------------------------------
Given the head of a singly linked list, rearrange the nodes so that
all nodes originally at odd positions (1st, 3rd, 5th, ...) come
first, followed by all nodes originally at even positions. Do this
in place, without allocating new nodes, while preserving the
relative order within each group.

Time:  O(n)
Space: O(1) extra
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head


def _to_list(head: Optional[ListNode]) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def _build(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    print(_to_list(odd_even_list(_build([1, 2, 3, 4, 5]))))  # expected output: [1, 3, 5, 2, 4]
    print(_to_list(odd_even_list(_build([2, 1, 3, 5, 6, 4, 7]))))  # expected output: [2, 3, 6, 7, 1, 5, 4]
    print(_to_list(odd_even_list(_build([]))))  # expected output: []
