"""
Linked List Cycle Detection
----------------------------------------------------------------
Given the head of a singly linked list, determine whether the
list contains a cycle. Uses Floyd's tortoise-and-hare technique:
two pointers advance through the list at different speeds, and a
cycle exists if and only if they eventually meet.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    print(has_cycle(a))
    # expected output: False

    c.next = a  # introduce a cycle back to the head
    print(has_cycle(a))
    # expected output: True

    print(has_cycle(None))
    # expected output: False
