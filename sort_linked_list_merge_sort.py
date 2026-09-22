"""
Sort a Linked List
--------------------
Given the head of a singly linked list, sort it in ascending order
and return the new head. Hit O(n log n) time with merge sort:
repeatedly split the list into two halves using the fast/slow
pointer trick, sort each half recursively, then merge the two sorted
halves back together.

Time:  O(n log n)
Space: O(log n) recursion stack
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    return _merge(left, right)


def _merge(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next

    tail.next = a if a else b
    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def from_list(values: list) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(sort_list(from_list([4, 2, 1, 3]))))       # expected output: [1, 2, 3, 4]
    print(to_list(sort_list(from_list([-1, 5, 3, 4, 0]))))    # expected output: [-1, 0, 3, 4, 5]
    print(to_list(sort_list(from_list([]))))                 # expected output: []
    print(to_list(sort_list(from_list([1]))))                # expected output: [1]
