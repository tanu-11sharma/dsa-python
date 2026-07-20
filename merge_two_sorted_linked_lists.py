"""
Merge Two Sorted Linked Lists
------------------------------
Given the heads of two singly linked lists that are each sorted in
non-decreasing order, splice their nodes together into a single sorted
linked list and return its head. The merge should be done in place by
relinking existing nodes rather than creating new ones.

Time:  O(n + m)
Space: O(1) (excluding the output list itself)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def merge_two_sorted_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def _build(values: list) -> Optional[ListNode]:
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def _to_list(node: Optional[ListNode]) -> list:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    print(_to_list(merge_two_sorted_lists(_build([1, 2, 4]), _build([1, 3, 4]))))
    # expected output: [1, 1, 2, 3, 4, 4]

    print(_to_list(merge_two_sorted_lists(_build([]), _build([]))))
    # expected output: []

    print(_to_list(merge_two_sorted_lists(_build([]), _build([0]))))
    # expected output: [0]

    print(_to_list(merge_two_sorted_lists(_build([5]), _build([1, 2, 3]))))
    # expected output: [1, 2, 3, 5]
