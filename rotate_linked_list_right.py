"""
Rotate Linked List to the Right
-------------------------------
Given the head of a singly linked list and a non-negative integer k, shift the
list to the right by k positions. Each shift moves the final node to the front.
Because the pattern repeats every len(list) shifts, k may safely exceed the
length of the list.

Time:  O(n)
Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Return the head of the list after rotating it right by k positions."""
    if head is None or head.next is None or k == 0:
        return head

    # Measure the list and close it into a ring.
    length = 1
    tail = head
    while tail.next is not None:
        tail = tail.next
        length += 1
    tail.next = head

    # The node that becomes the new tail sits length - k % length steps in.
    steps_to_new_tail = length - (k % length)
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


def build_list(values: List[int]) -> Optional[ListNode]:
    """Helper: turn a Python list into a linked list."""
    dummy = ListNode()
    cursor = dummy
    for value in values:
        cursor.next = ListNode(value)
        cursor = cursor.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    """Helper: turn a linked list back into a Python list."""
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    print(to_list(rotate_right(build_list([1, 2, 3, 4, 5]), 2)))
    # expected output: [4, 5, 1, 2, 3]

    print(to_list(rotate_right(build_list([0, 1, 2]), 4)))
    # expected output: [2, 0, 1]

    print(to_list(rotate_right(build_list([7]), 3)))
    # expected output: [7]

    print(to_list(rotate_right(build_list([]), 1)))
    # expected output: []
