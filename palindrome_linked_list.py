"""
Palindrome Linked List
----------------------
Given the head of a singly linked list, decide whether its values read
the same forwards and backwards. The check uses constant extra space:
a slow/fast pointer pair locates the middle, the second half is reversed
in place, and the two halves are then compared node by node.

Time:  O(n)
Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev: Optional[ListNode] = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True


def build(values: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


if __name__ == "__main__":
    print(is_palindrome(build([1, 2, 2, 1])))     # expected output: True
    print(is_palindrome(build([1, 2, 3, 2, 1])))  # expected output: True
    print(is_palindrome(build([1, 2, 3])))        # expected output: False
    print(is_palindrome(build([7])))              # expected output: True
