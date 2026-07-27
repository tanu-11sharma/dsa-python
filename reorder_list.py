"""
Reorder List
-------------
Given a singly linked list L0 -> L1 -> ... -> Ln-1 -> Ln, rearrange it
in place into L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... without
changing the node values, using only pointer manipulation.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def list_to_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # Find the middle of the list.
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half.
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # Merge the two halves.
    first, second = head, prev
    while second:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head


if __name__ == "__main__":
    print(list_to_values(reorder_list(build_list([1, 2, 3, 4]))))  # expected output: [1, 4, 2, 3]
    print(list_to_values(reorder_list(build_list([1, 2, 3, 4, 5]))))  # expected output: [1, 5, 2, 4, 3]
    print(list_to_values(reorder_list(build_list([1]))))  # expected output: [1]
    print(list_to_values(reorder_list(build_list([1, 2]))))  # expected output: [1, 2]
