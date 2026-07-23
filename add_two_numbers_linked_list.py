"""
Add Two Numbers (Linked List)
-------------------------------
Two non-negative integers are represented as linked lists where each node
holds a single digit, stored in reverse order (the 1's digit is the head
of the list). Add the two numbers and return the sum as a linked list in
the same reversed-digit format.

Time:  O(max(n, m)) where n, m are the lengths of the two lists
Space: O(max(n, m)) for the output list
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        current.next = ListNode(digit)
        current = current.next

    return dummy.next


def build_list(digits):
    dummy = ListNode()
    current = dummy
    for d in digits:
        current.next = ListNode(d)
        current = current.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print(to_list(add_two_numbers(l1, l2)))  # expected output: [7, 0, 8]

    l1 = build_list([9, 9])
    l2 = build_list([1])
    print(to_list(add_two_numbers(l1, l2)))  # expected output: [0, 0, 1]

    l1 = build_list([0])
    l2 = build_list([0])
    print(to_list(add_two_numbers(l1, l2)))  # expected output: [0]
